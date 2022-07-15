const router = require("express").Router();
const token = require("esprima");
const conexao = require('./bd_connection');



router.get("/", (req, res) => {
  res.render("index.ejs");
});

router.get('/visualizar/', (req, res) => {
  let query7 = `SELECT * from tbl_metricas where tbl_metricas.id_teste_de_mesa = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = '${req.query.apelido}')`;

  conexao.query(query7, (err, result) => {
    res.render("visualizar.ejs", {
      metricas: result
    });
  })
});



router.post("/", (req, res) => {
  //criação dos tokens para cada programa
  var tokensO = token.tokenize(req.body.programao, { loc: true })
  var tokensP = token.tokenize(req.body.programap, { loc: true })

  //define os vetores que serão preenchido com os valores de cada variavel de cada programa
  const vectorSend = [];
  const vectorO = [];
  const vectorP = [];
  //separa cada linha do código fonte e adiciona no array de linhas
  const linhasO = req.body.programao.split("\n").map((linha) => linha.trim());
  const linhasP = req.body.programap.split("\n").map((linha) => linha.trim());
  //query para chamadas das SP
    const query = `CALL insere_programa_o('${req.body.programao}', '${req.body.apelido}')`;
    const query2 = `CALL insere_programa_p('${req.body.programap}', '${req.body.apelido}')`;
    const query3 = `CALL insere_teste_de_mesa('${req.body.apelido}')`;

    conexao.query(query, (err, result) => {
        if (err) throw err;
    });
    conexao.query(query2, (err, result) => {
        if (err) throw err;
    });
    conexao.query(query3, (err, result) => {
        if (err) throw err;
    })
    //executa o código fonte preparado para o programa O.
    try{
      eval(preparaCodigoFonte(linhasO, tokensO,"_o"))
    }
    catch(err){
      console.log(err)
    }
   
    //aloca os valores de cada variavel no vetor de valores
    vectorSend.forEach((element) => {
      vectorO.push(element);
    })
    //zera o vetor auxiliar
    vectorSend.splice(0, vectorSend.length)
    
    //executa o código fonte preparado para o programa P.
    eval(preparaCodigoFonte(linhasP, tokensP, "_p"))

    //aloca os valores de cada variavel no vetor de valores
    vectorSend.forEach((element) => {
      vectorP.push(element);
    });

    
  var merge
  const vectorFull = []
  for(var i = 0; i < vectorO.length; i++){
    merge = { ...vectorO[i], ...vectorP[i]}
    vectorFull.push(merge)
  }
  
   vectorFull.forEach((element) => {
      let queryMetricas = `CALL insere_metricas('${element.variavel_o}', '${element.valor_o}','${element.linha_o}', '${element.variavel_p}', '${element.valor_p}', '${element.linha_p}','${req.body.apelido}')`;
      conexao.query(queryMetricas, (err, result) => {
        
        if (err){
          console.log("erro capturado ao salvar métricas:"+ err)
        };
       
      }
      );
    })
  res.redirect("/visualizar/?apelido="+req.body.apelido);

  
});




function preparaCodigoFonte(linhas, tokens,programa) {
  var newCodigoFonte 
   
  //para cada atualização de variaveis, ou seja, 
  //quando o token for um =, ver qual foi o token anterior e se for um identificador mostra o valor da variavel atraves do eval
  tokens.forEach((token) => {
      //Verifica se há uma definição de função
      if(token.value == "function"){
        //se houver, separa os parâmetros, pula uma linha e coloca no vetor os valores dos parametros
         var parametros = linhas[token.loc.start.line-1].split("(")[1].split(")")[0].split(",") 
          parametros.forEach((parametro)=>{
              linhas[token.loc.start.line-1] += ` \n vectorSend.push({variavel${programa}: '${parametro}', valor${programa}: ${parametro}, linha${programa}:'${linhas[token.loc.start.line - 1] }'} )` 
          })   
      }
      //se houver uma atribuição de variavel, verifica se o token anterior é um identificador
      if (token.type == "Punctuator") {
          if (token.value == "=") {
              var anterior = tokens[tokens.indexOf(token) - 1]
              if(anterior.value == "]"){
                /*é necessário essa verificação e esse for para tratar
                  o caso de uma atribuição de um array.
                  Ex: arr[1+variavel] = 0
                  Ocorre um erro no token anterior ao =, pois o token anterior ao = é um ]. Por isso um laço foi necessário
                */
              
                  for(let i = 1; i < tokens.indexOf(token)-1; i++){
                      if(tokens[tokens.indexOf(token)-i-1].value=="["){
                          anterior = tokens[tokens.indexOf(token)-i-2]
                          break
                      }
                  }
              }
              /* Após isso, verificamos se encontramos um identificador, ou seja, uma variável */
              if (anterior.type == "Identifier") {
                  //se encontramos, e a variavel é um array, adicionamos o valor de cada posição no vetor que será enviado para o BD
                  //se não, adicionamos o valor da variável no vetor que será enviado para o BD
                  linhas[token.loc.start.line - 1] += `\n
                  if(Array.isArray(${anterior.value})){
                      for(var i = 0; i < ${anterior.value}.length; i++){
                          vectorSend.push({variavel${programa}: '${anterior.value}'+[i], valor${programa}: ${anterior.value}[i], linha${programa}:'${linhas[token.loc.start.line - 1] }' })
                      }
                  }
                  else{
                    vectorSend.push({
                          variavel${programa}: '${anterior.value}', 
                          valor${programa}: ${anterior.value}, 
                          linha${programa}: '${linhas[token.loc.start.line - 1] }'
                         })
                  }
                   `
                   //adiciona as alterações no codigo fonte a variavel
                  newCodigoFonte = linhas.join("\n")
              }
          }
      }
  })
  
  //retorna o codigo fonte com as alterações
  return newCodigoFonte
}
  
module.exports = router;
