const express = require('express');
const bodyParser = require('body-parser');
const logger = require('morgan');

import Events from './models/events';
import Characters from './models/characters';

// SETUP
// ===================================

const app = express();
const port = process.env.PORT || 8080;
const events = new Events();
const characters = new Characters();

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
    if (req.query.startWith) {
      events.getStartingBy(req.query.startWith)
        .then(events => res.json(events))
        .catch(err => res.send(err));
    } else {
      events.getAll()
        .then(events => res.json(events))
        .catch(err => res.send(err));
    }
  });

router.route('/events/:marvelId')
  .get((req, res) => {
    events.getById(req.params.marvelId)
      .then(event => res.json(event))
      .catch(err => res.send(err));
  });

router.route('/characters')
  .get((req, res) => {
    if (req.query.startWith) {
      characters.getStartingBy(req.query.startWith)
        .then(characters => res.json(characters))
        .catch(err => res.send(err));
    } else {
      characters.getAll()
        .then(characters => res.json(characters))
        .catch(err => res.send(err));
    }
  });

router.route('/characters/:marvelId')
  .get((req, res) => {
    characters.getById(req.params.marvelId)
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
