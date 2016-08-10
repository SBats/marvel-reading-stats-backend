import express = require("express");
import Comics from '../models/comics';

let router: ComicsRoutes;
export default class ComicsRoutes {
  comics: Comics = null;

  constructor() {
    router = this;
    router.comics = new Comics();
  }

  all(req: any, res: any): void {
    if (req.query.startWith) {
      router.comics.getStartingBy(req.query.startWith)
        .then(comics => res.json(comics))
        .catch(err => res.send(err));
    } else {
      router.comics.getAll()
        .then(comics => res.json(comics))
        .catch(err => res.send(err));
    }
  }

  byId(req: any, res: any): void {
    router.comics.getById(req.params.marvelId)
      .then(comic => res.json(comic))
      .catch(err => res.send(err));
  };
};
