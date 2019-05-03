from SQLAlchemy.Connection.Connection import Connection
from SQLAlchemy.model.Employee import Employee
from SQLAlchemy.model.Department import Department
from SQLAlchemy.model.Project import Project
from SQLAlchemy.model.Location import Location
from SQLAlchemy.repositorio.Department_Rep import DepartmentRep
from SQLAlchemy.repositorio.Employee_Rep import EmployeeRep
from SQLAlchemy.repositorio.Location_Rep import LocationRep
from SQLAlchemy.repositorio.Project_Rep import ProjectRep
from SQLAlchemy.validate import Validate

validate = Validate()

while True:
    print(30*'-', 'MENU', 30*'-')
    print('1 - Employee\n2 - Department\n3 - Project \n4 - Location\n 0 - EXIT')
    choice = int(input('Pick one option:\n'))
    if choice == 0:
        break

    elif choice == 1:
        Con = Connection()
        session = Con.session()
        emp_rep = EmployeeRep()
        emp_choice = int(input('1 - Register Employee\n2 - Delete Employee\n'
                               '3 - List all employees \n4 - Find one employee\n0 - Cancel\n'))

        if emp_choice == 1:
            name = input('Enter you name:\n')
            cpf = input('Enter you CPF:\n')
            email = input('Enter an valid email:\n')
            phone = input('Enter your phone:\n')
            job = input('Enter your job:\n')
            salary = float(input('Enter your salary:\n'))

            if validate.cpf_is_valid(cpf) and validate.email_is_valid(email):
                emp = Employee(name=name, cpf=cpf, email=email, phone=phone, job=job, salary=salary)
                print(emp_rep.create(emp, session))
            else:
                print('Email or CPF invalid, going over!\n')

        elif emp_choice == 2:
            emp_id = int(input('Enter the employee ID to delete::\n'))
            print(emp_rep.delete(emp_id, session))

        elif emp_choice == 3:
            print(emp_rep.select_all(session))

        elif emp_choice == 4:
            emp_id = int(input('Enter the employee ID to find:\n'))
            print(emp_rep.select_one(emp_id, session))

        else:
            print('Invalid option, exiting now...')
            break

    elif choice == 2:
        Con = Connection()
        session = Con.session()
        dep_rep = DepartmentRep()
        dep_choice = int(input('1 - New Department\n2 - Delete Department\n'
                               '3 - List all departments\n4 - Find one department\n0 - Cancel\n'))

        if dep_choice == 1:
            name = input('Enter the department name:\n')
            manager_id = int(input('Enter the manager ID\n'))
            location_id = int(input('Enter the location ID\n'))
            dep = Department(name, manager_id, location_id)
            print(dep_rep.create(dep, session))

        elif dep_choice == 2:
            dep_id = int(input('Enter the department ID\n'))
            print(dep_rep.delete(dep_id, session))

        elif dep_choice == 3:
            print(dep_rep.select_all(session))

        elif dep_choice == 4:
            dep_id = int(input('Enter the department ID to find:\n'))
            print(dep_rep.select_one(dep_id, session))

        else:
            print('Invalid option, exiting now...')
            break

    elif choice == 3:
        Con = Connection()
        session = Con.session()
        proj_rep = ProjectRep()
        proj_choice = int(input('1 - New Project\n2 - Delete Project\n3 -List all project'
                                ' \n4 - Find one project\n0 - Cancel\n'))
        if proj_choice == 1:
            name = input("Enter the project's name:\n")
            manager_id = int(input('Enter the manager ID:\n'))
            dt_limit = input('Enter the limit date(YYYY-MM-DD):\n')
            proj = Project(name=name, manager_id=manager_id, dt_limit=dt_limit)
            print(proj_rep.create(proj, session))

        elif proj_choice == 2:
            proj_id = int(input('Enter the project ID to delete:\n'))
            print(proj_rep.delete(proj_id, session))

        elif proj_choice == 3:
            print(proj_rep.select_all(session))

        elif proj_choice == 4:
            proj_id = int(input('Enter the project ID to find:\n'))
            print(proj_rep.select_one(proj_id, session))

        else:
            print('Invalid option, exiting now...')
            break

    elif choice == 4:
        Con = Connection()
        session = Con.session()
        loc_rep = LocationRep()
        loc_choice = int(input('1 - New Location\n2 - Delete Location\n'
                               '3 - List all locations \n4 - Find one location\n0 - Cancel\n'))
        if loc_choice == 1:
            address = input('Enter the Address:\n')
            postal_code = input('Enter the postal code:\n')
            city = input('Enter the city name:\n')
            state = input('Enter the sate:\n')
            loc = Location(address, postal_code, city, state)
            print(loc_rep.create(loc, session))

        elif loc_choice == 2:
            loc_id = int(input('Enter the location ID to delete:\n'))
            print(loc_rep.delete(loc_id, session))

        elif loc_choice == 3:
            print(loc_rep.select_all(session))

        elif loc_choice == 4:
            loc_id = int(input('Enter the location ID to find:\n'))
            print(loc_rep.select_one(loc_id, session))

        else:
            print('Invalid option, exiting now...')
            break
