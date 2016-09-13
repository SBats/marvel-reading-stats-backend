import DatabaseService from '../services/database';

export default class Characters {
  dbService: DatabaseService = null;

  constructor() {
    this.dbService = new DatabaseService();
  }

  getAll(): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('characters')
          .find(
            {},
            {'name': 1, 'marvelId': 1, _id: 0}
          )
          .sort([['name', 1]])
          .toArray()
          .then((characters: any) => {
            db.close();
            return characters;
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
        return db.collection('characters')
          .find(
            {'name': {$regex: `^${query}`, $options: 'i'}},
            {'name': 1, 'marvelId': 1, _id: 0}
          )
          .sort([['name', 1]])
          .toArray()
          .then((characters: any) => {
            db.close();
            return characters;
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
        return db.collection('characters')
          .find({'marvelId': parseInt(marvelId, 10)}, {
            _id: 0,
            'name': 1,
            'description': 1,
            'urls': 1,
            'thumbnail': 1,
            'marvelId': 1,
          })
          .limit(1)
          .next()
          .then((character: any) => {
            db.close();
            return character;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }
}
