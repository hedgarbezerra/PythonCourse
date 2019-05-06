from SQLAlchemy.Connection import db


class EmployeeQuery:

    @staticmethod
    def create(employee, session):
        session.add(employee)

    @staticmethod
    def update(employee_id, employee, session):
        session.query(db.Employee).filter(db.Employee.employee_id == employee_id).update({'name': employee.name,
                                                                                          'cpf': employee.cpf,
                                                                                          'email': employee.email,
                                                                                          'phone': employee.phone,
                                                                                          'job': employee.job,
                                                                                          'salary': employee.salary})

    @staticmethod
    def select_one(employee_id, session):
        employee = session.query(db.Employee).get(employee_id)
        return employee

    @staticmethod
    def select_all(session):
        employees = session.query(db.Employee).all()
        return employees

    @staticmethod
    def select_cpf(employee_cpf, session):
        employee = session.query(db.Employee).filter(db.Employee.cpf == employee_cpf).one()
        return employee

    @staticmethod
    def delete(employee_id, session):
        session.query(db.Employee).filter(db.Employee.employee_id == employee_id).delete()

