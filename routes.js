const router = require("express").Router();

//document html require

router.get('/', (req, res) => {
    res.render('index.ejs');
})

//the body receive the code from the user and send to the server to be applied an regex to separate the variables and operatos
router.post('/', (req, res) => {
    let body = req.body;
    let code = body.codigo;
    let regex = /[0-9]+|[+-/*]/g;
    let array = code.match(regex);
    let result = 0;
    let words = req.body.codigo.split(regex);
    console.log(words);
    console.log(array);
}
)

module.exports = router;