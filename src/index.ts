const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectId;
const bodyParser = require('body-parser');
const logger = require('morgan');


// SETUP
// ===================================

const config = require('./config.json');

const app = express();
const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.send('Please select a collection, eg., /collections/messages');
});


// START
// ===================================

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
