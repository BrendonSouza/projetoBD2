const router = require("express").Router();

//document html require

router.get('/', (req, res) => {
    res.render('index.ejs');
})

router.get('/table', (req, res) => {
    res.render('table.ejs');
})

module.exports = router;