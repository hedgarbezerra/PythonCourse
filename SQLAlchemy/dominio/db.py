from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from SQLAlchemy.Connection.Connection import Connection


database = Connection().connect()
Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String(30), nullable=False)
    manager_id = Column(Integer, ForeignKey('employee.employee_id'))
    location_id = Column(Integer, ForeignKey('location.location_id'))

    def __repr__(self):
        return f"Departmente #{self.department_id} nomeado: {self.department_name}"


class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(Integer)
    job = Column(String(10))
    salary = Column(Float(12, 2))

    def __repr__(self):
        return f"Employee {self.name} register under #{self.employee_id}ID,  Contact:{self.phone}/ {self.email}"


class Location(Base):
    __tablename__ = 'location'
    location_id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    postal_code = Column(Integer, nullable=False)
    city = Column(String(30))
    state = Column(String(20))

    def __repr__(self):
        return f"Addres: {self.address} on {self.city}-{self.state} // Postal Code: {self.postal_code}"


Base.metadata.create_all(database)

