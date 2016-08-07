import express = require("express");
import Events from '../models/events';

let router: EventsRoutes;
export default class EventsRoutes {
  events: Events = null;

  constructor() {
    router = this;
    router.events = new Events();
  }

  all(req: any, res: any): void {
    console.log(router);
    if (req.query.startWith) {
      router.events.getStartingBy(req.query.startWith)
        .then(events => res.json(events))
        .catch(err => res.send(err));
    } else {
      router.events.getAll()
        .then(events => res.json(events))
        .catch(err => res.send(err));
    }
  }

  byId(req: any, res: any): void {
    router.events.getById(req.params.marvelId)
      .then(event => res.json(event))
      .catch(err => res.send(err));
  };
};
