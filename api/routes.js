const router = require('express').Router()
var token = require('esprima')
//const conexao = require('./bd_connection');

router.get('/', (req, res) => {
    res.send('Home')
}) 

router.post('/enterCode', (req, res) => {
    const bodyData = req.body
    //try {
        const codeTokensO = token.tokenize(bodyData.codigoO,  { loc: true })
        var linesO = bodyData.codigoO.split("\n").map((line) => line.trim())

        const codeTokensP = token.tokenize(bodyData.codigoSecundario, { loc: true })
        var linesP = bodyData.codigoSecundario.split("\n").map((line) => line.trim())
        
        const vectorSend = [];
        const vectorO = [];
        const vectorP = [];

        const query = `CALL insere_programa_o('${bodyData.programao}')`;
        const query2 = `CALL insere_programa_p('${bodyData.programap}')`;
        conexao.query(query, (err, result) => {
            if (err) throw err;
            console.log(result);
        });
        conexao.query(query2, (err, result) => {
            if (err) throw err;
            console.log(result);
        });
        const query3 = `CALL insere_teste_de_mesa('teste 2')`;
        conexao.query(query3, (err, result) => {
            if (err) throw err;
            console.log(result);
        })
        
        
    
        (manipulateSourceCode(linesO, codeTokensO,"_o"))
        //copy values from vectorSend to vectorO
        vectorSend.forEach((element) => {
            vectorO.push(element);
            }
        );
        vectorSend.splice(0, vectorSend.length)
        (manipulateSourceCode(linesP, codeTokensP, "_p"))
    
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
                if (err) throw err;
                console.log(result);
                }
            );
        })
        
        return res.status(200).json(codeTokensO)

    //} catch (error) {
    //     return res.status(400).json(error)
    //}
})

function manipulateSourceCode(lines, tokens) {
    
    const vectorSend = [];
    var newCode 
    //para cada atualização de variaveis, ou seja, quando o token for um =, ver qual foi o token anterior e se for um identificador mostra o valor da variavel atraves do eval
    tokens.forEach((token) => {
        
        if(token.value == "function"){
           var params = lines[token.loc.start.line-1].split("(")[1].split(")")[0].split(",") 
            params.forEach((param)=>{
                lines[token.loc.start.line-1] += ` \n vectorSend.push({variavel: '${param}', valor: ${param}})` 
            })   
        }
        if (token.type == "Punctuator") {
            if (token.value == "=") {
                var previous = tokens[tokens.indexOf(token) - 1]
                if(previous.value == "]"){
                    for(let i = 1; i < 5; i++){
                        if(tokens[tokens.indexOf(token)-i-1].value=="["){
                            previous = tokens[tokens.indexOf(token)-i-2]
                            break
                        }
                    }
                }
                if (previous.type == "Identifier") {
                    lines[token.loc.start.line - 1] += `\n
                    if(Array.isArray(${previous.value})){
                        for(var i = 0; i < ${previous.value}.length; i++){
                            vectorSend.push({variavel: '${previous.value}'+[i], valor: ${previous.value}[i]})
                        }
                    }
                    else{
                        vectorSend.push({
                            variavel: '${previous.value}', 
                            valor: ${previous.value}, 
                            linha: '${lines[token.loc.start.line - 1] }'
                           })
                    }
                     `
                    newCode = lines.join("\n")
                }
            }
        }
    })
    
    return newCode
}

module.exports = router