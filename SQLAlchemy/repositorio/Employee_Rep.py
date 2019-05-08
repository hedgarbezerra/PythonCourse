import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Employee_query import EmployeeQuery
from SQLAlchemy.Connection.db import Employee
from SQLAlchemy.model.Employee import Employee as Emp
from SQLAlchemy.Connection.Department_query import DepartmentQuery


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
    def select_cpf(employee_cpf, session):
        query = EmployeeQuery()
        try:
            employees = query.select_cpf(employee_cpf, session)
            return employees
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_all(session):
        query = EmployeeQuery()
        try:
            employees = query.select_all(session)
            return employees
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def create(employee, session):
        query = EmployeeQuery()
        dep = DepartmentQuery()
        department = dep.select_one(employee.department_id, session)
        employee = Employee(name=employee.name, cpf=employee.cpf, email=employee.email, phone=employee.phone,
                            job=employee.job, salary=employee.salary, department_id=employee.department_id, department=department)
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

    def obj_list(self, session):
        employees = []
        for obj in self.select_all(session):
            employee = Emp(employee_id=obj.employee_id, name=obj.name, cpf=obj.cpf, email=obj.email,
                           phone=obj.phone, job=obj.job, salary=obj.salary)
            employees.append(employee)
        return employees
