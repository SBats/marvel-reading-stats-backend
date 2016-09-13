import DatabaseService from '../services/database';

export default class Comics {
  dbService: DatabaseService = null;

  constructor() {
    this.dbService = new DatabaseService();
  }

  getAll(): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getStartingBy(query: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {'title': {$regex: `^${query}`, $options: 'i'}},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getAllBySeries(seriesId: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {'series.resourceURI': {$regex: `/${seriesId}$`, $options: 'i'}},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getAllByCharacter(characterId: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {'characters.items.resourceURI': {$regex: `/${characterId}$`, $options: 'i'}},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getAllByEvent(eventId: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {'events.items.resourceURI': {$regex: `/${eventId}$`, $options: 'i'}},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getAllByCreator(creatorId: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find(
            {'creators.items.resourceURI': {$regex: `/${creatorId}$`, $options: 'i'}},
            {'title': 1, 'marvelId': 1, 'thumbnail': 1, 'urls': 1, _id: 0}
          )
          .sort([['title', 1]])
          .toArray()
          .then((comics: any) => {
            db.close();
            return comics;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getById(marvelId: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('comics')
          .find({'marvelId': parseInt(marvelId, 10)}, {
            _id: 0,
            'title': 1,
            'description': 1,
            'urls': 1,
            'thumbnail': 1,
            'marvelId': 1,
          })
          .limit(1)
          .next()
          .then((comic: any) => {
            db.close();
            return comic;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }
}
