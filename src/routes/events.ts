import Events from '../models/events';
import Comics from '../models/comics';

let router: EventsRoutes;
export default class EventsRoutes {
  events: Events = null;
  comics: Comics = null;

  constructor() {
    router = this;
    router.events = new Events();
    router.comics = new Comics();
  }

  all(req: any, res: any): void {
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
    const eventId = req.params.marvelId;
    let result: any = null;
    router.events.getById(eventId)
      .then(event => result = event)
      .then(() => router.comics.getAllByEvent(eventId))
      .then(comics => result.comics = comics)
      .then(() => res.json(result))
      .catch(err => res.send(err));
  }
}
