const router = require("express").Router();
const token = require("esprima");
//const conexao = require('./bd_connection');

router.get("/", (req, res) => {
  res.render("index.ejs");
});

router.post("/", (req, res) => {
  var tokensO = token.tokenize(req.body.programao, { loc: true })
  var tokensP = token.tokenize(req.body.programap, { loc: true })

  const vareval = [];
  const vetOriginal = [];
  const vetProd = [];
  
  const linoriginal = req.body.original.split("\n").map((linha) => linha.trim());
  const linproducao = req.body.producao.split("\n").map((linha) => linha.trim());
    const inoriginal = `CALL insere_programa_o('${req.body.original}')`;
    const inproducao = `CALL insere_programa_p('${req.body.producao}')`;
    
    conexao.query(inoriginal, (err, result) => {
        if (err) throw err;
        console.log(result);
    });
    conexao.query(inproducao, (err, result) => {
        if (err) throw err;
        console.log(result);
    });
    const query3 = `CALL insere_teste_de_mesa('${req.body.apelido}')`;
    conexao.query(query3, (err, result) => {
        if (err) throw err;
        console.log(result);
    })  
    
    eval(organizaprograma(linoriginal, tokensO,"_o"))
   //copy values from vareval to vetOriginal
    vareval.forEach((element) => {
      vetOriginal.push(element);
    }
    );
    vareval.splice(0, vareval.length)
    eval(organizaprograma(linproducao, tokensP, "_p"))

    vareval.forEach((element) => {
      vetProd.push(element);
    }
    );
    
    var merge
    const vectorFull = []
    for(var i = 0; i < vetOriginal.length; i++){
      merge = { ...vetOriginal[i], ...vetProd[i]}
      vectorFull.push(merge)
    }
    
    vectorFull.forEach((element) => {
      let queryMetricas = `CALL insere_metricas('${element.variavel_o}', '${element.valor_o}','${element.linha_o}', '${element.variavel_p}', '${element.valor_p}', '${element.linha_p}','${req.body.apelido}')`;
      conexao.query(queryMetricas, (err, result) => {
        if (err) throw err;
        console.log(result);
      }
      );
    })

  
});

function organizaprograma(linhas, tokens,programa) {
  var newCodigoFonte 
   
  //para cada atualização de variaveis, ou seja, quando o token for um =, ver qual foi o token anterior e se for um identificador mostra o valor da variavel atraves do eval
  tokens.forEach((token) => {
      
      if(token.value == "function"){
         var parametros = linhas[token.loc.start.line-1].split("(")[1].split(")")[0].split(",") 
          parametros.forEach((parametro)=>{
              linhas[token.loc.start.line-1] += ` \n vareval.push({variavel${programa}: '${parametro}', valor${programa}: ${parametro}, linha${programa}:'${linhas[token.loc.start.line - 1] }' )` 
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
                          vareval.push({variavel${programa}: '${anterior.value}'+[i], valor${programa}: ${anterior.value}[i]})
                      }
                  }
                  else{
                    vareval.push({
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