import DatabaseService from '../services/database';

export default class Users {
  dbService: DatabaseService = null;

  constructor() {
    this.dbService = new DatabaseService();
  }

  create(email: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('users')
          .insertOne({
            'email': email,
            'name': email.split('@')[0],
            'collection': []
          })
          .then((user: any) => {
            db.close();
            return user;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  delete(email: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('users')
          .deleteOne({'email': email})
          .then((user: any) => {
            db.close();
            return user;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }

  getByEmail(email: string): Promise<any> {
    return this.dbService.connect()
      .then((db: any) => {
        return db.collection('users')
          .find({'email': email}, {
            _id: 0,
            'email': 1,
            'name': 1,
            'collection': 1
          })
          .limit(1)
          .next()
          .then((user: any) => {
            db.close();
            return user;
          })
          .catch((err: any) => {
            db.close();
            return err;
          });
      })
      .catch((err: any) => err);
  }
}
