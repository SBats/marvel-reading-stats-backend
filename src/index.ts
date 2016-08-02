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
const dbUrl = config.dbUrl;
const collectionsList = [
  'comics',
  'events',
  'series',
  'creators',
  'characters',
];


// MIDDLEWARES
// ===================================

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(logger('dev'));


// ROUTES
// ===================================

const router = express.Router();

router.get('/', (req, res) => {
  res.json({message: 'Please select a collection, eg., /collections/messages'});
});

app.use('/', router);


// START
// ===================================

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
