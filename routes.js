const router = require("express").Router();
const token = require("esprima");
const conexao = require('./bd_connection');

const ponctuatorAllow = [
  "!=",
  "==",
  ">",
  "<",
  ">=",
  "<=",
  "&&",
  "||",
  "++",
  "--",
  "+",
  "-",
  "*",
  "/",
  "%",
  "=",
];


router.get("/", (req, res) => {
  res.render("index.ejs");
});

router.post("/", (req, res) => {
  const parser = token.tokenize(req.body.programao, { loc: true });
  const vectorSend = [];
  const linhas = req.body.programao.split("\n").map((linha) => linha.trim());
    // const query = `CALL insere_programa_o('${req.body.programao}')`;
    // const query2 = `CALL insere_programa_p('${req.body.programap}')`;
    // conexao.query(query, (err, result) => {
    //     if (err) throw err;
    //     console.log(result);
    // });
    // conexao.query(query2, (err, result) => {
    //     if (err) throw err;
    //     console.log(result);
    // });
    // const query3 = `CALL insere_teste_de_mesa('teste 1')`;
    // conexao.query(query3, (err, result) => {
    //     if (err) throw err;
    //     console.log(result);
    // })
    
  parser.forEach((token) => {
    if (token.type == "Punctuator") {
      if (ponctuatorAllow.includes(token.value)) {
        vectorSend.push({
          variavel: token.value,
          linha: linhas[token.loc.start.line - 1],
        });
      }
    } else if (token.type != "Keyword") {
      //convert token.value to hex
      const hex = token.value.charCodeAt(0).toString(16);
      vectorSend.push(
        vectorSend.push({
          variavel: token.value,
          linha: linhas[token.loc.start.line - 1],
        })
      );
    }
  });
  vectorSend.forEach((token) => {
    if (typeof token == "number") {
      vectorSend.splice(vectorSend.indexOf(token), 1);
    }
  });

  console.log(vectorSend);
});

/*
function verifyArr(token,linhas){
  linhas.forEach((linha) => {
    const peaceLet = `let ${token}`;
    const peaceVar = `var ${token}`;
    const peaceConst = `const ${token}`;
    if(linha.includes(peaceLet)){
      const a1=eval(`${linha}\n if(Array.isArray(${peace.replace("let","")})){  ${peace.replace("let","")}.length } else{0}`);
      console.log(a1)
    }
    else if(linha.includes(peaceVar)){
      const a2=eval(`${linha}\n if(Array.isArray(${peace.replace("var","")})){  ${peace.replace("var","")}.length } else{0}`);
      console.log(a2)
    }
    else if(linha.includes(peaceConst)){
      const a3=eval(`${linha}\n if(Array.isArray(${peace.replace("const","")})){  ${peace.replace("const","")}.length } else{0}`);
      console.log(a3)
    }
  })
}
*/
module.exports = router;
