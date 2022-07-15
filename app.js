// Configurações de variáveis de ambiente
var express = require("express");
var esprima  = require('esprima');
var _eval  = require('incremental-eval');
var app = express();
var db = require("./db/db.js");
app.set("engine ejs", "ejs");
app.use(express.urlencoded({extended: false}));


// Definição dos operadores reconhecidos no teste de mesa
const operadores = [
    "!",
    "!=",
    "==",
    "===",
    ">",
    "<",
    ">=",
    "<=",
    "~",
    "<<",
    ">>",
    ">>>",
    "<<=",
    ">>=",
    ">>>=",
    "&",
    "|",
    "^",
    "&=",
    "|=",
    "^=",
    "?",
    "&&",
    "||",
    "++",
    "--",
    "+",
    "+=",
    "-",
    "-=",
    "*",
    "*=",
    "/",
    "/=",
    "%",
    "%=",
    "**",    
    "="
];

// Definição de palavras reservadas para não serem confundidas como variáveis
// no if 'identifier'
const reservadas = ['console', 'log'];


// Função que recebe como parâmetro o número da linha que está sendo analisada e o código dela,
// insere no banco de dados e retorna o id da linha inserida
async function insere_linha(n_linha, item){
    return new Promise(resolve => {
        // Declaração do insert no bd
        const i_ln = "INSERT INTO linha (numero, codigo) VALUES (?, ?);";

        // Execução do insert
        db.query(i_ln, [n_linha, item], function(err, data){
            if (err) {
                return console.error(err.message);
            }
            resolve(data.insertId);
        });
    });
}

// Função que recebe como parametros um programa (codigo), o id do teste de mesa associado a esse programa
// e o parametro de controle (0: insere na tabela dados_programa_o | 1: insere na tabela dados_programa_p)
async function analisa_programa(programa, id_tm, pc){
    // Declaração da chamada da stored procedure e algumas variáveis auxiliares
    const p_id = "CALL insere_dados(?, ?, ?, ?, ?);";
    var id_linha = 0;
    var codigo = "";
    var flag = 0;
    var inicio = 0;

    // Separa o codigo do programa em linhas
    var linhas = programa.split(/\r\n/);

    // Para cada linha faz a análise
    for(var i = 0; i < linhas.length; i++){
        item = linhas[i];

        // Vetor para verificar as variáveis já analisadas na linha
        variaveis = [];

        // Insere a linha no banco de dados e salva o id dela
        id_linha = await insere_linha(i + 1, item);

        // Identifica os tokens da linha
        var tokens = esprima.tokenize(item);

        // Define como código a ser executado todas as linhas do início até a atual
        codigo = linhas.slice(0, i+1).join('');

        // Tratamento para blocos de código
        // Se for uma abertura de bloco de código salva o começo do bloco e adiciona uma flag
        if (item.slice(-1) == "{" ){
            if(flag == 0){
                inicio = i;
            }
            flag++;
        }

        // Tratamento para blocos de código
        // Se for um fechamento de bloco de código retira uma flag, verifica se o bloco de código
        // com o escopo mais externo foi fechado (flag == 0) e, caso verdadeiro, atualiza o codigo e
        // os tokens para serem referentes ao bloco inteiro e não apenas a linha
        if (item.slice(-1) == "}" ){
            flag--;

            if (flag == 0){
                var fim = i+1;
                var bloco = linhas.slice(inicio, fim);
                codigo = linhas.slice(0, fim).join('');
                tokens = esprima.tokenize(bloco.join(''));
            }  
        }

        // Analisa cada token da lista de tokens e faz o tratamento
        tokens.forEach(function(item){
            var val = 0;

            // Se o token já estiver na lista de variáveis analisadas nessa linha, retorna
            // caso contrario adiciona o token
            if (variaveis.includes(item.value)){
                return;
            } else{
                variaveis.push(item.value);
            }

            // Verifica se o token é um identificador 'Identifier' e se não é uma palavra reservada
            // Nesse caso o identificador é possívelmente uma variável
            if (item.type == 'Identifier' && !reservadas.includes(item.value)){
                // Se o bloco de código de escopo mais amplo já foi fechado (flag == 0) 
                // executa a linha para obter o valor da variável
                if(flag == 0){
                    val = _eval(codigo + " exports." + item.value + " = " + item.value);
                }
                
                // Insere a variável e o seu valor no banco de dados
                db.query(p_id, [item.value, val, id_tm, id_linha, pc], function(err){
                    if (err) {
                        return console.error(err.message);
                    } 
                });
            } else if (item.type == 'Punctuator' && operadores.includes(item.value)){
                // Verifica se o token é um sinal 'Punctuator' e se está presente na lista de operadores
                // permitidos
                // Nesse caso o token é um operador

                // Converte o simbolo do operador em seu código da tabela ascii, esse vai ser seu valor
                // no banco de dados
                val = item.value.charCodeAt(0);

                // Insere o operador e seu valor no banco de dados
                db.query(p_id, [item.value, val, id_tm, id_linha, pc], function(err){
                    if (err) {
                        return console.error(err.message);
                    }
                });
            }else{
                // Se não for variável ou operador retorna
                return;
            }
        });
    }
}

// Rotas..
app.get("/", function(req, res){  
    // Faz um select nos testes de mesa do banco de dados
    const sql = "SELECT *, DATE_FORMAT(data_tm, '%d/%m/%Y - %H:%i') AS data_tm FROM teste_mesa ORDER BY id_tm DESC;";
    db.query(sql, [], function(err, rows) {
        if (err) {
            return console.error(err.message);
        }
        res.render("index.ejs", { dados: rows });
    })
});

app.get("/deletar/:id_tm", function(req, res){
    // Deleta um teste de mesa
    const sql = "CALL deleta_tm(?)";
    db.query(sql, [req.params.id_tm], function(err) {
        if (err) {
            return console.error(err.message);
        }
        res.redirect("/");
    })
});

app.get("/inserir", function(req, res){
    // Carrega a página de inserção de teste de mesa
    res.render("inserir.ejs");
});

app.post("/inserir", function(req, res){
    // Insere o teste de mesa, caso de teste, programas o e p e chama a função que analisa os códigos
    var id_po, id_pp, id_ct, id_tm;

    // Declaração das queries
    const i_po = "INSERT INTO programa_o (data_codificacao, codigo) VALUES (CURRENT_TIMESTAMP(), ?);";
    const i_pp = "INSERT INTO programa_p (data_codificacao, codigo) VALUES (CURRENT_TIMESTAMP(), ?);";
    const i_ct = "INSERT INTO caso_teste (id_po, id_pp) VALUES (?, ?);";
    const i_tm = "INSERT INTO teste_mesa (data_tm, id_ct) VALUES (CURRENT_TIMESTAMP(), ?);";

    // Executa as queries em cadeia
    // Executa a query que insere os programas O e P no banco de dados
    db.query(i_po + i_pp, [req.body.programa_o, req.body.programa_p], function(err, data) {
        if (err) {
            return console.error(err.message);
        }

        // Recupera o id de inserção dos programas O e P
        id_po = data[0].insertId;
        id_pp = data[1].insertId;

        // Executa a query que insere o caso de teste no banco de dados
        db.query(i_ct, [id_po, id_pp], function(err, data) {
            if (err) {
                return console.error(err.message);
            }
    
            // Recupera o id de inserção do caso de teste
            id_ct = data.insertId;

            // Executa a query que insere o teste de mesa no banco de dados
            db.query(i_tm, [id_ct], function(err, data) {
                if (err) {
                    return console.error(err.message);
                }

                // Recupera o id de inserção do teste de mesa
                id_tm = data.insertId;

                // Chama a função para analisar os códigos O e P e redireciona para a página de resultado
                (async function(){
                    await analisa_programa(req.body.programa_o, id_tm, 0);
                    await analisa_programa(req.body.programa_p, id_tm, 1);
                })().then(resolve => {
                    res.redirect("/resultado/" + id_tm + '/' + 1);
                });
            });
        });
    });
});

app.get("/resultado/:id_tm/:n_linha", function(req, res){
    // Exibe o resultado de uma análise linha a linha

    // Declaração das queries
    const s_linhas_o = "SELECT * FROM programa_o WHERE id_po IN (SELECT id_po FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = ?));";
    const s_dados_o = "SELECT * FROM dados_tm_o WHERE id_tm = ? AND id_linha IN (SELECT id_linha FROM linha WHERE numero = ?);";
    const s_linhas_p = "SELECT * FROM programa_p WHERE id_pp IN (SELECT id_pp FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = ?));";
    const s_dados_p = "SELECT * FROM dados_tm_p WHERE id_tm = ? AND id_linha IN (SELECT id_linha FROM linha WHERE numero = ?);";

    // Faz um select:
    // nos códigos do programa O e do programa P
    // nos dados salvos linha a linha do programa O e do programa P
    db.query(s_linhas_o + s_dados_o + s_linhas_p + s_dados_p, [req.params.id_tm, req.params.id_tm, req.params.n_linha, req.params.id_tm, req.params.id_tm, req.params.n_linha], function(err, rows) {
        if (err) {
            return console.error(err.message);
        }

        res.render("resultado.ejs", {
            programa_o: rows[0][0].codigo.split(/\r\n/),
            dados_o: rows[1],
            programa_p: rows[2][0].codigo.split(/\r\n/),
            dados_p: rows[3],
            linha: req.params.n_linha,
            id_tm: req.params.id_tm,
        });
    });
});

app.listen(3000, () => {
    console.log('SERVIDOR ATIVO, ACESSE http://localhost:3000');
});