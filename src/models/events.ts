import DatabaseService from '../services/database';

export default class Events {
  dbService: DatabaseService = null;

  constructor() {
    this.dbService = new DatabaseService();
  }

  getAll(): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        console.log('connected to db !');
        return db.collection('events').find({}, {"title": 1, "marvelId": 1, _id: 0}).sort([['title', 1]]).toArray()
          .then((events: any) => {
            db.close();
            return events;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }
}