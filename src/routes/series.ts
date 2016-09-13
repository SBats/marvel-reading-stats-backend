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
    let result: any = null;
    router.series.getById(seriesId)
      .then(series => result = series)
      .then(() => router.comics.getAllBySeries(seriesId))
      .then(comics => result.comics = comics)
      .then(() => res.json(result))
      .catch(err => res.send(err));
  }
}
