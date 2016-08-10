const express = require('express');
const bodyParser = require('body-parser');
const logger = require('morgan');

import EventsRoutes from './routes/events';
import CharactersRoutes from './routes/characters';
import ComicsRoutes from './routes/comics';
import CreatorsRoutes from './routes/creators';
import SeriesRoutes from './routes/series';
import UsersRoutes from './routes/users';


// SETUP
// ===================================

const app = express();
const port = process.env.PORT || 8080;
const events = new EventsRoutes();
const characters = new CharactersRoutes();
const comics = new ComicsRoutes();
const creators = new CreatorsRoutes();
const series = new SeriesRoutes();
const users = new UsersRoutes();

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

router.route('/series').get(series.all);
router.route('/series/:marvelId').get(series.byId);

router.route('/users/:email').get(users.getByEmail);
router.route('/users/:email').post(users.create);
router.route('/users/:email').delete(users.delete);

router.get('/', (req: any, res: any) => {
  res.json({message: 'Welcome to MRS API !'});
});

router.get('*', (req: any, res: any) => {
  res.send(`404 - Damn Ultron stall this resource!`, 404);
});

app.use('/', router);


// START
// ===================================

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
