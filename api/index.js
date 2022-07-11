const express = require('express')
const app = express()
const port = 3001

var routes = require('./routes')

app.use(express.json())


app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});

app.use(routes)

app.listen(port, () => {
    console.log(`Rodando na porta: ${port}`)
})
