import express = require("express");
import Series from '../models/series';
import Comics from '../models/comics';

let router: SeriesRoutes;
export default class SeriesRoutes {
  series: Series = null;
  comics: Comics = null;

  constructor() {
    router = this;
    router.series = new Series();
    router.comics = new Comics();
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
    const seriesId = req.params.marvelId;
    router.series.getById(seriesId)
      .then(series => {
        const result = series;
        router.comics.getAllBySeries(seriesId)
          .then(comics => {
            result.comics = comics;
            res.json(result);
          })
          .catch(err => res.send(err));
      })
      .catch(err => res.send(err));
  };
};
