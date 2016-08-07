import DatabaseService from '../services/database';

export default class Series {
  dbService: DatabaseService = null;

  constructor() {
    this.dbService = new DatabaseService();
  }

  getAll(): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('series')
          .find(
            {},
            {"name": 1, "marvelId": 1, _id: 0}
          )
          .sort([['name', 1]])
          .toArray()
          .then((series: any) => {
            db.close();
            return series;
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
        return db.collection('series')
          .find(
            {"name": {$regex: `^${query}`, $options: "i"}},
            {"name": 1, "marvelId": 1, _id: 0}
          )
          .sort([['name', 1]])
          .toArray()
          .then((series: any) => {
            db.close();
            return series;
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
        return db.collection('series')
          .find({"marvelId": parseInt(marvelId)}, {
            _id: 0,
            "name": 1,
            "description": 1,
            "urls": 1,
            "thumbnail": 1,
            "marvelId": 1,
          })
          .limit(1)
          .next()
          .then((series: any) => {
            db.close();
            return series;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }
}