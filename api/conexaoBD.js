var mysql = require('mysql2');

var conexao = mysql.createConnection({
    host: '172.17.0.4',
    user: 'root',
    password: 'mysql',
    database: 'teste_de_mesa',
    port: 3306,
});

conexao.connect();
module.exports = conexao;