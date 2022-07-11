const router = require("express").Router();
const token = require("esprima");
const conexao = require('./bd_connection');



router.get("/", (req, res) => {
  res.render("index.ejs");
});

// router.get('/visualizar/:apelido', (req, res) => {
//   conexao.query(`SELECT * from tbl_metricas where tbl_metricas.id_teste_de_mesa = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = "${req.params.apelido}")`, (err, result) => {
  
//      console.log(result)
//     }
//   );
// }
// );

router.post("/", (req, res) => {
  var tokensO = token.tokenize(req.body.programao, { loc: true })
  var tokensP = token.tokenize(req.body.programap, { loc: true })

  const vectorSend = [];
  const vectorO = [];
  const vectorP = [];
  
  const linhasO = req.body.programao.split("\n").map((linha) => linha.trim());
  const linhasP = req.body.programap.split("\n").map((linha) => linha.trim());
    const query = `CALL insere_programa_o('${req.body.programao}', '${req.body.apelido}')`;
    const query2 = `CALL insere_programa_p('${req.body.programap}', '${req.body.apelido}')`;
    
    conexao.query(query, (err, result) => {
        if (err) throw err;
        console.log(result);
    });
    conexao.query(query2, (err, result) => {
        if (err) throw err;
        console.log(result);
    });
    const query3 = `CALL insere_teste_de_mesa('${req.body.apelido}')`;
    conexao.query(query3, (err, result) => {
        if (err) throw err;
        console.log(result);
    })
    eval(preparaCodigoFonte(linhasO, tokensO,"_o"))
   //copy values from vectorSend to vectorO
    vectorSend.forEach((element) => {
      vectorO.push(element);
    }
    );
    vectorSend.splice(0, vectorSend.length)
    eval(preparaCodigoFonte(linhasP, tokensP, "_p"))

    vectorSend.forEach((element) => {
      vectorP.push(element);
    }
    );
    
    var merge
    const vectorFull = []
    for(var i = 0; i < vectorO.length; i++){
      merge = { ...vectorO[i], ...vectorP[i]}
      vectorFull.push(merge)
    }
    
    vectorFull.forEach((element) => {
      let queryMetricas = `CALL insere_metricas('${element.variavel_o}', '${element.valor_o}','${element.linha_o}', '${element.variavel_p}', '${element.valor_p}', '${element.linha_p}','${req.body.apelido}')`;
      conexao.query(queryMetricas, (err, result) => {
        res.redirect('/#visualizar')
        if (err) throw err;
        console.log(result);
      }
      );
    })

  
});

function preparaCodigoFonte(linhas, tokens,programa) {
  var newCodigoFonte 
   
  //para cada atualização de variaveis, ou seja, quando o token for um =, ver qual foi o token anterior e se for um identificador mostra o valor da variavel atraves do eval
  tokens.forEach((token) => {
      
      if(token.value == "function"){
         var parametros = linhas[token.loc.start.line-1].split("(")[1].split(")")[0].split(",") 
          parametros.forEach((parametro)=>{
              linhas[token.loc.start.line-1] += ` \n vectorSend.push({variavel${programa}: '${parametro}', valor${programa}: ${parametro}, linha${programa}:'${linhas[token.loc.start.line - 1] }' )` 
          })   
      }
      if (token.type == "Punctuator") {
          if (token.value == "=") {
              var anterior = tokens[tokens.indexOf(token) - 1]
              if(anterior.value == "]"){
                  for(let i = 1; i < 15; i++){
                      if(tokens[tokens.indexOf(token)-i-1].value=="["){
                          anterior = tokens[tokens.indexOf(token)-i-2]
                          break
                      }
                  }
              }
              if (anterior.type == "Identifier") {
                  linhas[token.loc.start.line - 1] += `\n
                  if(Array.isArray(${anterior.value})){
                      for(var i = 0; i < ${anterior.value}.length; i++){
                          vectorSend.push({variavel${programa}: '${anterior.value}'+[i], valor${programa}: ${anterior.value}[i]})
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
                  newCodigoFonte = linhas.join("\n")
              }
          }
      }
  })
  
  return newCodigoFonte
  }
  
module.exports = router;
