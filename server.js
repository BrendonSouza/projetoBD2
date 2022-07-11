const express = require("express");
const token = require("esprima");
const app = express();
const port = 2522;
const fs = require("fs");
const router = require("./routes");

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));
app.use(router);

app.listen(port, () => {
  console.log(`Aplicação executando na porta ${port}`);
});


