from SQLAlchemy.dominio.db import Employee
from SQLAlchemy.Connection.Connection import Connection
import locale


class Employee:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def __init__(self, name, cpf, email, phone=None, job=None, salary=None):
        self.__employee_id = None
        self.__cpf = cpf
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__job = job
        self.__salary = salary

    def __repr__(self):
        return f"Employee {self.__name} register under #ID {self.__employee_id} ~ Job: {self.__job} ~" \
            f" Salary:{locale.currency(self.__salary, grouping=True)}  // Contact:{self.__phone}/ {self.__email}"

    @property
    def id(self):
        return self.__employee_id

    @id.setter
    def id(self, value):
        self.__employee_id  = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        self.__job = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

