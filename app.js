var express = require("express");
var esprima  = require('esprima');
var _eval  = require('incremental-eval');
var app = express();
var db = require("./db/db.js");
app.set("engine ejs", "ejs");
app.use(express.urlencoded({extended: false}));

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

const reservadas = ['console', 'log'];

async function insere_linha(n_linha, item){
    return new Promise(resolve => {
        const i_ln = "INSERT INTO linha (numero, codigo) VALUES (?, ?);";
        db.query(i_ln, [n_linha, item], function(err, data){
            if (err) {
                return console.error(err.message);
            }
            resolve(data.insertId);
        });
    });
}

async function analisa_programa(programa, pc, id_tm){
    const p_id = "CALL insere_dados(?, ?, ?, ?, ?);";
    var id_linha = 0;
    var codigo = "";
    var flag = 0;
    var inicio = 0;
    var linhas = programa.split(/\r\n/);

    for(var i = 0; i < linhas.length; i++){
        item = linhas[i];
        id_linha = await insere_linha(i + 1, item);
        var tokens = esprima.tokenize(item);
        variaveis = [];

        codigo = linhas.slice(0, i+1).join('');

        if (item.slice(-1) == "{" ){
            if(flag == 0){
                inicio = i;
            }
            flag++;
        }

        if (item.slice(-1) == "}" ){
            flag--;

            if (flag == 0){
                var fim = i+1;
                var bloco = linhas.slice(inicio, fim);
                codigo = linhas.slice(0, fim).join('');
                tokens = esprima.tokenize(bloco.join(''));
            }  
        }

        tokens.forEach(function(item){
            var val = 0;

            if (variaveis.includes(item.value)){
                return;
            } else{
                variaveis.push(item.value);
            }

            if (item.type == 'Identifier' && !reservadas.includes(item.value)){
                if(flag == 0){
                    val = _eval(codigo + " exports." + item.value + " = " + item.value);
                }
            
                db.query(p_id, [item.value, val, id_tm, id_linha, pc], function(err){
                    if (err) {
                        return console.error(err.message);
                    } 
                });
            } else if (item.type == 'Punctuator' && operadores.includes(item.value)){
                val = item.value.charCodeAt(0);
                db.query(p_id, [item.value, val, id_tm, id_linha, pc], function(err){
                    if (err) {
                        return console.error(err.message);
                    }
                });
            }else{
                return;
            }
        });
    }
}

//rotas..
app.get("/", function(req, res){  
    const sql = "SELECT *, DATE_FORMAT(data_tm, '%d/%m/%Y - %H:%i') AS data_tm FROM teste_mesa ORDER BY id_tm DESC;";
    db.query(sql, [], function(err, rows) {
        if (err) {
            return console.error(err.message);
        }
        res.render("index.ejs", { dados: rows });
    })
});

app.get("/deletar/:id_tm", function(req, res){  
    const sql = "CALL deleta_tm(?)";
    db.query(sql, [req.params.id_tm], function(err) {
        if (err) {
            return console.error(err.message);
        }
        res.redirect("/");
    })
});

app.get("/inserir", function(req, res){
    res.render("inserir.ejs");
});

app.post("/inserir", function(req, res){
    var id_po, id_pp, id_ct, id_tm;

    const i_po = "INSERT INTO programa_o (data_codificacao, codigo) VALUES (CURRENT_TIMESTAMP(), ?);";
    const i_pp = "INSERT INTO programa_p (data_codificacao, codigo) VALUES (CURRENT_TIMESTAMP(), ?);";
    const i_ct = "INSERT INTO caso_teste (id_po, id_pp) VALUES (?, ?);";
    const i_tm = "INSERT INTO teste_mesa (data_tm, id_ct) VALUES (CURRENT_TIMESTAMP(), ?);";

    db.query(i_po + i_pp, [req.body.programa_o, req.body.programa_p], function(err, data) {
        if (err) {
            return console.error(err.message);
        }

        id_po = data[0].insertId;
        id_pp = data[1].insertId;

        db.query(i_ct, [id_po, id_pp], function(err, data) {
            if (err) {
                return console.error(err.message);
            }
    
            id_ct = data.insertId;

            db.query(i_tm, [id_ct], function(err, data) {
                if (err) {
                    return console.error(err.message);
                }

                id_tm = data.insertId;
                (async function(){
                    await analisa_programa(req.body.programa_o, 0, id_tm);
                    await analisa_programa(req.body.programa_p, 1, id_tm);
                })().then(resolve => {
                    res.redirect("/resultado/" + id_tm + '/' + 1);
                });
            });
        });
    });
});

app.get("/resultado/:id_tm/:n_linha", function(req, res){
    const s_linhas_o = "SELECT * FROM programa_o WHERE id_po IN (SELECT id_po FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = ?));";
    const s_dados_o = "SELECT * FROM dados_tm_o WHERE id_tm = ? AND id_linha IN (SELECT id_linha FROM linha WHERE numero = ?);";

    const s_linhas_p = "SELECT * FROM programa_p WHERE id_pp IN (SELECT id_pp FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = ?));";
    const s_dados_p = "SELECT * FROM dados_tm_p WHERE id_tm = ? AND id_linha IN (SELECT id_linha FROM linha WHERE numero = ?);";

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