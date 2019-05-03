import locale

from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Table, DECIMAL, Date, NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from SQLAlchemy.Connection.Connection import Connection

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
database = Connection().connect()
Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String(30), nullable=False)
    manager_id = Column(Integer, ForeignKey('employee.employee_id'))
    location_id = Column(Integer, ForeignKey('location.location_id'))

    def __repr__(self):
        return f"Departmente #{self.department_id} nomeado: {self.department_name}\n"


class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(15))
    job = Column(String(10))
    salary = Column(NUMERIC(precision=10, scale=2))
    """
    emp_proj = relationship('emp_proj')
    project = relationship('project')
    department = relationship('department')"""

    def __repr__(self):
        return f"Employee {self.name} register under #ID {self.employee_id} ~ Job: {self.job} ~" \
            f" Salary:{locale.currency(self.salary, grouping=True)}  // Contact:{self.phone}/ {self.email}\n"


class Location(Base):
    __tablename__ = 'location'
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(50), nullable=False)
    postal_code = Column(String(10), nullable=False)
    city = Column(String(30))
    state = Column(String(20))

    #department = relationship('department')

    def __repr__(self):
        return f"Addres: {self.address} on {self.city}-{self.state} // Postal Code: {self.postal_code}\n"


class Project(Base):
    __tablename__ = 'project'
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(30), nullable=False)
    manager_id = Column(Integer, ForeignKey('employee.employee_id'))
    dt_start = Column(Date, default=func.sysdate())
    dt_limit = Column(Date)

    #emp_proj = relationship('emp_proj')

    def __repr__(self):
        return f'Project #{self.project_id} - {self.name} //' \
            f' Project through {self.dt_start} ~ {self.dt_limit}\n'


"""EmpProj = Table('emp_proj', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employee.employee_id'), primary_key=True),
    Column('project_id', Integer, ForeignKey('project.project_id'), primary_key=True))
"""

Base.metadata.create_all(database)

