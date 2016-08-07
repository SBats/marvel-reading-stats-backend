import express = require("express");
import Creators from '../models/creators';

let router: CreatorsRoutes;
export default class CreatorsRoutes {
  creators: Creators = null;

  constructor() {
    router = this;
    router.creators = new Creators();
  }

  all(req: any, res: any): void {
    console.log(router);
    if (req.query.startWith) {
      router.creators.getStartingBy(req.query.startWith)
        .then(creators => res.json(creators))
        .catch(err => res.send(err));
    } else {
      router.creators.getAll()
        .then(creators => res.json(creators))
        .catch(err => res.send(err));
    }
  }

  byId(req: any, res: any): void {
    router.creators.getById(req.params.marvelId)
      .then(creator => res.json(creator))
      .catch(err => res.send(err));
  };
};
