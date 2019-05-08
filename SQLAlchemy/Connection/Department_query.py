from sqlalchemy.orm import joinedload

from SQLAlchemy.Connection import db


class DepartmentQuery:

    @staticmethod
    def create(department, session):
        session.add(department)

    @staticmethod
    def delete(department_id, session):
        session.query(db.Department).filter(db.Department.department_id == department_id).delete()

    @staticmethod
    def update(department_id, department, session):
        session.query(db.Department).filter(db.Department.department_id == department_id).update({
                                                    'department_name': department.department_name,
                                                    'manager_id': department.manager_id,
                                                    'location_id': department.location_id})

    @staticmethod
    def select_one(department_id, session):
        department = session.query(db.Department).get(department_id)
        return department

    @staticmethod
    def select_all(session):
        departments = session.query(db.Department).options(joinedload(db.Department.manager)).all()
        return departments

    @staticmethod
    def select_name(department_name, session):
        departments = session.query(db.Department).filter(db.Department.department_name == department_name).all()
        return departments
