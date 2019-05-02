from SQLAlchemy.Connection.Connection import Connection
from SQLAlchemy.model.Employee import Employee
from SQLAlchemy.model.Department import Department
from SQLAlchemy.model.Project import Project
from SQLAlchemy.model.Location import Location
from SQLAlchemy.repositorio.Employee_Rep import EmployeeRep
import locale
from SQLAlchemy.validate import Validate

Con = Connection()
session = Con.session()
emp_rep = EmployeeRep()
validate = Validate()

print(emp_rep.delete(2, session))
"""
while True:
    print(30*'-', 'MENU', 30*'-')
    print('1 - Employee\n2 - Department\n3 - Project \n4 - Location\n 0 - EXIT')
    a = 1
    #int(input('Pick one option:\n'))
    if a == 0:
        break
    elif a == 1:
        name = input('Enter you name:\n')
        cpf = '212.332.123-32'
        #input('Enter you CPF:\n')
        email = 'wqheuhiew@gmail.com'
        #input('Enter an valid email:\n')
        if validate.cpf_is_valid(cpf) and validate.email_is_valid(email):
            emp = Employee(name=name, cpf=cpf, email=email)
            emp.salary = float(12900.00)
            emp.job = 'MKT'
            print(emp)
        else:
            print('aaa')
        break
    elif a == 2:
        dep = Department()

    elif a == 3:
        proj = Project()

    elif a == 4:
        loc = Location()

#print(emp_rep.create(emp, session))
#print(emp_rep.create(emp2, session))
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#print(locale.currency(emp.salary, grouping=True))
#print(emp_rep.update(1, emp, session))

"""
