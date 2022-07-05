const express = require("express");
const token = require("esprima");
const app = express();
const port = 2522;
const router = require("./routes");
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));
app.use(router);


var codigoFonte = `
function binarySearch(arr, l, r, x){
  if (r >= l) {
      let mid = l + Math.floor((r - l) / 2);
      if (arr[mid] == x)
          return mid;
      if (arr[mid] > x)
          return binarySearch(arr, l, mid - 1, x);
      return binarySearch(arr, mid + 1, r, x);
  }
  return -1;
}

let arr = [ 2, 3, 4, 10, 40 ];
let x = 10;
let n = arr.length
let result = binarySearch(arr, 0, n - 1, x);

`


var tokens = token.tokenize(codigoFonte, { loc: true })
var linhas = codigoFonte.split("\n").map((linha) => linha.trim())

function preparaCodigoFonte(linhas, tokens) {
var newCodigoFonte 
//para cada atualização de variaveis, ou seja, quando o token for um =, ver qual foi o token anterior e se for um identificador mostra o valor da variavel atraves do eval
tokens.forEach((token) => {
    if (token.type == "Punctuator") {
        if (token.value == "=") {
            const anterior = tokens[tokens.indexOf(token) - 1]
            if (anterior.type == "Identifier") {
             //adiciona um console.log no codigoFonte e executa no eval
                linhas[token.loc.start.line - 1] += `\nconsole.log("${anterior.value} ="+${anterior.value})`
                newCodigoFonte = linhas.join("\n")
            }
        }
    }
})
//copy values from console.logs to variaveis


//print values from variaveis

return newCodigoFonte
}
preparaCodigoFonte(linhas, tokens)
app.listen(port, () => {
  console.log(`Aplicação executando na porta ${port}`);
});
