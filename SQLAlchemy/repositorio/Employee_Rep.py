import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Employee_query import EmployeeQuery
from SQLAlchemy.dominio.db import Employee


class EmployeeRep:

    @staticmethod
    def select_one(employee_id, session):
        query = EmployeeQuery()
        try:
            employee = query.select_one(employee_id, session)
            return employee
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_all(session):
        query = EmployeeQuery()
        employees = query.select_all(session)
        return employees

    @staticmethod
    def create(employee, session):
        query = EmployeeQuery()
        employee = Employee(name=employee.name, cpf=employee.cpf, email=employee.email, phone=employee.phone,
                            job=employee.job, salary=employee.salary)
        try:
            query.create(employee, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Employee registered sucessfully!'
        finally:
            session.close()

    @staticmethod
    def update(employee_id, employee, session):
        query = EmployeeQuery()
        try:
            query.update(employee_id, employee, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Employee sucessfully updated!'
        finally:
            session.close()

    @staticmethod
    def delete(employee_id, session):
        query = EmployeeQuery()
        try:
            query.delete(employee_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Employee sucessfully deleted!'
        finally:
            session.close()

