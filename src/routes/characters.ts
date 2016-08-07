import express = require("express");
import Characters from '../models/characters';

let router: CharactersRoutes;
export default class CharactersRoutes {
  characters: Characters = null;

  constructor() {
    router = this;
    router.characters = new Characters();
  }

  all(req: any, res: any): void {
    console.log(router);
    if (req.query.startWith) {
      router.characters.getStartingBy(req.query.startWith)
        .then(characters => res.json(characters))
        .catch(err => res.send(err));
    } else {
      router.characters.getAll()
        .then(characters => res.json(characters))
        .catch(err => res.send(err));
    }
  }

  byId(req: any, res: any): void {
    router.characters.getById(req.params.marvelId)
      .then(character => res.json(character))
      .catch(err => res.send(err));
  };
};
