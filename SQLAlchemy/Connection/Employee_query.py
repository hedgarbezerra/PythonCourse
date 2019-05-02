from SQLAlchemy.dominio import db
from SQLAlchemy.model import Employee


class EmployeeQuery:

    @staticmethod
    def create(employee, session):
        session.add(employee)

    @staticmethod
    def update(employee_id, employee, session):
        session.query(db.Employee).filter(db.Employee.employee_id == employee_id).update({'name': employee.name,
                                     'cpf': employee.cpf, 'email': employee.email,
                                     'phone': employee.phone, 'job': employee.job, 'salary': employee.salary})

    @staticmethod
    def select_one(employee_id, session):
        session.query(db.Employee).get(employee_id)

    @staticmethod
    def delete(employee_id, session):
        session.query(db.Employee).filter(db.Employee.employee_id == employee_id).delete()
