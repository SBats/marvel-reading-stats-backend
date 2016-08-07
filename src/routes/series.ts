import express = require("express");
import Series from '../models/series';

let router: SeriesRoutes;
export default class SeriesRoutes {
  series: Series = null;

  constructor() {
    router = this;
    router.series = new Series();
  }

  all(req: any, res: any): void {
    console.log(router);
    if (req.query.startWith) {
      router.series.getStartingBy(req.query.startWith)
        .then(series => res.json(series))
        .catch(err => res.send(err));
    } else {
      router.series.getAll()
        .then(series => res.json(series))
        .catch(err => res.send(err));
    }
  }

  byId(req: any, res: any): void {
    router.series.getById(req.params.marvelId)
      .then(series => res.json(series))
      .catch(err => res.send(err));
  };
};
