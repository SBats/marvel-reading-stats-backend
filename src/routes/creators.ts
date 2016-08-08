import express = require("express");
import Creators from '../models/creators';
import Comics from '../models/comics';

let router: CreatorsRoutes;
export default class CreatorsRoutes {
  creators: Creators = null;
  comics: Comics = null;

  constructor() {
    router = this;
    router.creators = new Creators();
    router.comics = new Comics();
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
    const creatorId = req.params.marvelId;
    router.creators.getById(creatorId)
      .then(creator => {
        const result = creator;
        router.comics.getAllByCreator(creatorId)
          .then(comics => {
            result.comics = comics;
            res.json(result);
          })
          .catch(err => res.send(err));
      })
      .catch(err => res.send(err));
  };
};
