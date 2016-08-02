const express = require('express');
const bodyParser = require('body-parser');
const logger = require('morgan');

import Events from './models/events';

// SETUP
// ===================================

const app = express();
const port = process.env.PORT || 8080;
const events = new Events();

// MIDDLEWARES
// ===================================

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(logger('dev'));


// ROUTES
// ===================================

const router = express.Router();

router.route('/events')
  .get((req, res) => {
    events.getAll()
      .then(events => res.json(events))
      .catch(err => res.send(err));
  });

router.route('/events/:marvelId')
  .get((req, res) => {
    events.getById(req.params.marvelId)
      .then(event => res.json(event))
      .catch(err => res.send(err));
  });

router.get('/', (req, res) => {
  res.json({message: 'Welcome to MRS API !'});
});

app.use('/', router);


// START
// ===================================

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
