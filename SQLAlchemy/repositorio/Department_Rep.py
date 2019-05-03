from SQLAlchemy.Connection.Department_query import DepartmentQuery
import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.dominio.db import Department


class DepartmentRep:

    @staticmethod
    def create(department, session):
        query = DepartmentQuery()
        department = Department(department_name=department.department_name,
                                manager_id=department.manager_id, location_id=department.location_id)
        try:
            query.create(department, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Department registered sucessfully!'
        finally:
            session.close()

    @staticmethod
    def update(department_id, department, session):
        query = DepartmentQuery()
        try:
            query.update(department_id, department, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Department updated sucessfully!'
        finally:
            session.close()

    @staticmethod
    def delete(department_id, session):
        query = DepartmentQuery()
        try:
            query.delete(department_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Department deleted sucessfully!'
        finally:
            session.close()
