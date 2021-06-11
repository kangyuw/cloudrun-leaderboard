const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());

app.post('/', function (req, res) {
  console.log(req.body);
  /*
  You should return a json response with the following format:
  {
    "username": "Kang",        //The registered username
    "flag": "jplOsDIaFLhcMRlS" //The 16-word random generated string
  }
  */
  const response = "";
  res.send(response);
});

app.listen(process.env.PORT || 8080);
