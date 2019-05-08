from SQLAlchemy.Connection.Department_query import DepartmentQuery
import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.db import Department
from SQLAlchemy.repositorio.Employee_Rep import EmployeeRep
from SQLAlchemy.model.Department import Department as Dep
from SQLAlchemy.repositorio.Location_Rep import LocationRep


class DepartmentRep:

    @staticmethod
    def create(department, manager_cpf, postal_code, session):
        query = DepartmentQuery()
        emp_rep = EmployeeRep()
        loc_rep = LocationRep()
        location = loc_rep.select_postal_code(postal_code, session)
        employee = emp_rep.select_cpf(manager_cpf, session)
        department = Department(department_name=department.department_name, manager_id=employee.employee_id,
                                location_id=location.location_id, location=location, manager=employee)
        try:
            query.create(department, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, MySQLdb.DatabaseError) as e:
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

    @staticmethod
    def select_one(department_id, session):
        query = DepartmentQuery()
        try:
            department = query.select_one(department_id, session)
            return department
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_name(department_name, session):
        query = DepartmentQuery()
        try:
            departments = query.select_name(department_name, session)
            return departments
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_all(session):
        query = DepartmentQuery()
        try:
            departments = query.select_all(session)
            return departments
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    def obj_list(self, session):
        departments = []
        for obj in self.select_all(session):
            department = Dep(department_id=obj.department_id, department_name=obj.department_name,
                             manager_id=obj.manager_id, location_id=obj.location_id)
            departments.append(department)
        return departments

