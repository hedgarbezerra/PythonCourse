import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Location_query import LocationQuery
from SQLAlchemy.Connection.db import Location
from SQLAlchemy.model.Location import Location as Loc


class LocationRep:

    @staticmethod
    def create(location, session):
        query = LocationQuery()
        location = Location(address=location.address, postal_code=location.postal_code, city=location.city, state=location.state)
        try:
            query.create(location, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Location registered sucessfully!'
        finally:
            session.close()

    @staticmethod
    def update(location_id, location, session):
        query = LocationQuery()
        try:
            query.update(location_id, location, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Location sucessfully updated!'
        finally:
            session.close()

    @staticmethod
    def delete(location_id, session):
        query = LocationQuery()
        try:
            query.delete(location_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Location sucessfully deleted!'
        finally:
            session.close()

    @staticmethod
    def select_one(location_id, session):
        query = LocationQuery()
        try:
            location = query.select_one(location_id, session)
            return location
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_postal_code(postal_code, session):
        query = LocationQuery()
        try:
            location = query.select_postal_code(postal_code, session)
            return location
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_all(session):
        query = LocationQuery()
        try:
            locations = query.select_all(session)
            return locations
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    def obj_list(self, session):
        locations = []
        for obj in self.select_all(session):
            location = Loc(location_id= obj.location_id, address=obj.address, postal_code=obj.postal_code,
                           city=obj.city, state=obj.state)
            locations.append(location)
        return locations

