import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Location_query import LocationQuery
from SQLAlchemy.dominio.db import Location


class LocationRep:

    @staticmethod
    def select(location_id, session):
        query = LocationQuery()
        try:
            query.select(location_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

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

