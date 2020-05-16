//Dependencias
const express = require("express");
const morgan = require("morgan");
const app = express();
const path = require("path");

//Middlewares
app.set('port', process.env.PORT || 3000);
app.use(morgan('dev'));
app.use(express.json());
app.use(express.static(path.join(__dirname,'../dist/')));

//Routes
app.get('/*/', (req, res, error) => {
    res.sendFile(path.join(__dirname,'../dist/index.html'));
})

//Start
app.listen(app.get('port'), () => {
    console.log("Stating server " + app.get('port'));
})