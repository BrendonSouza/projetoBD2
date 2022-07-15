// Configura a conexão no bd
var mysql = require("mysql");

var conexao = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "bd_metrica_ate",
    multipleStatements: true
});

conexao.connect();
module.exports = conexao;