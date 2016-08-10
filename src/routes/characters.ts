import express = require("express");
import Characters from '../models/characters';
import Comics from '../models/comics';

let router: CharactersRoutes;
export default class CharactersRoutes {
  characters: Characters = null;
  comics: Comics = null;


  constructor() {
    router = this;
    router.characters = new Characters();
    router.comics = new Comics();
  }

  all(req: any, res: any): void {
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
    const characterId = req.params.marvelId;
    router.characters.getById(characterId)
      .then(character => {
        const result = character;
        router.comics.getAllByCharacter(characterId)
          .then(comics => {
            result.comics = comics;
            res.json(result);
          })
          .catch(err => res.send(err));
      })
      .catch(err => res.send(err));
  };
};
