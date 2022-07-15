var mysql = require('mysql');

var conexao = mysql.createConnection({
    host: '172.17.0.3',
    user: 'root',
    password: '123456',
    database: 'teste_de_mesa',
    port: 3306,
});

conexao.connect();
module.exports = conexao;