from SQLAlchemy.Connection import db


class LocationQuery:

    @staticmethod
    def create(location, session):
        session.add(location)

    @staticmethod
    def update(location_id, location, session):
        session.query(db.Location).filter(db.Location.location_id == location_id
                                          ).update({'address': location.addres,
                                          'postal_code': location.postal_code,
                                          'city': location.city,
                                          'state': location.state})

    @staticmethod
    def delete(location_id, session):
        session.query(db.Location).filter(db.Location.location_id == location_id).delete()

    @staticmethod
    def select_one(location_id, session):
        location = session.query(db.Location).get(location_id)
        return location

    @staticmethod
    def select_all(session):
        locations = session.query(db.Location).all()
        return locations

    @staticmethod
    def select_postal_code(postal_code, session):
        locations = session.query(db.Location).filter(db.Location.postal_code == postal_code).one()
        return locations
