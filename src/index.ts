const express = require('express');
const bodyParser = require('body-parser');
const logger = require('morgan');

import EventsRoutes from './routes/events';
import CharactersRoutes from './routes/characters';
import ComicsRoutes from './routes/comics';
import CreatorsRoutes from './routes/creators';


// SETUP
// ===================================

const app = express();
const port = process.env.PORT || 8080;
const events = new EventsRoutes();
const characters = new CharactersRoutes();
const comics = new ComicsRoutes();
const creators = new CreatorsRoutes();

// MIDDLEWARES
// ===================================

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(logger('dev'));


// ROUTES
// ===================================

const router = express.Router();

router.route('/events').get(events.all);
router.route('/events/:marvelId').get(events.byId);

router.route('/characters').get(characters.all);
router.route('/characters/:marvelId').get(characters.byId);

router.route('/comics').get(comics.all);
router.route('/comics/:marvelId').get(comics.byId);

router.route('/creators').get(creators.all);
router.route('/creators/:marvelId').get(creators.byId);

router.get('/', (req: any, res: any) => {
  res.json({message: 'Welcome to MRS API !'});
});

app.use('/', router);


// START
// ===================================

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
