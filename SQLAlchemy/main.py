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
            fname = input('Enter you first name:\n').title()
            lname = input('Enter you last name:\n').title()
            cpf = input('Enter you CPF:\n')
            if not validate.cpf_is_valid(cpf):
                print('Invalid input, try again:\n')
                break
            email = input('Enter an valid email:\n').lower()
            if not validate.email_is_valid(email):
                print('Invalid input, try again:\n')
                break
            department_id = int(input('Department ID\n'))
            phone = input('Enter your phone:\n')
            job = input('Enter your job:\n').upper()
            salary = float(input('Enter your salary:\n'))
            name = fname+' '+lname
            emp = Employee(name=name, cpf=validate.cpf_convertion(cpf), email=email, department_id=department_id,
                           phone=phone, job=job, salary=salary)
            print(emp_rep.create(emp, session))

        elif emp_choice == 2:
            emp_id = int(input('Enter the employee ID to delete::\n'))
            print(emp_rep.delete(emp_id, session))

        elif emp_choice == 3:
            print(emp_rep.select_all(session))

        elif emp_choice == 4:
            find_emp = int(input('1 - Find by ID 2 - Find by CPF\n'))

            if find_emp == 1:
                emp_id = int(input('Enter the employee ID to find:\n'))
                print(emp_rep.select_one(emp_id, session))

            elif find_emp == 2:
                emp_name = input('Enter the employee CPF to find:\n')
                print(emp_rep.select_name(emp_name, session))

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
            name = input('Enter the department name:\n').title()
            manager_cpf = int(input('Enter the manager CPF:\n'))
            postalcode = int(input('Enter the location postal code:\n'))
            dep = Department(name)
            print(dep_rep.create(dep, manager_cpf, postalcode, session))

        elif dep_choice == 2:
            dep_id = int(input('Enter the department ID\n'))
            print(dep_rep.delete(dep_id, session))

        elif dep_choice == 3:
            print(dep_rep.select_all(session))

        elif dep_choice == 4:
            find_dep = int(input('1 - Find by ID 2 - Find by name\n'))
            if find_dep == 1:
                dep_id = int(input('Enter the department ID to find:\n'))
                print(dep_rep.select_one(dep_id, session))

            elif find_dep == 2:
                dep_name = input('Enter the department name to find:\n')
                print(dep_rep.select_name(dep_name, session))

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
            name = input("Enter the project's name:\n").title()
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
            find_proj = int(input('1 - Find by ID 2 - Find by name\n'))
            if find_proj == 1:
                proj_id = int(input('Enter the project ID to find:\n'))
                print(proj_rep.select_one(proj_id, session))

            elif find_proj == 2:
                proj_name = input('Enter the project name to find:\n')
                print(proj_rep.select_name(proj_name, session))

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
            address = input('Enter the Address:\n').title()
            postal_code = input('Enter the postal code:\n')
            city = input('Enter the city name:\n').title()
            state = input('Enter the state:\n').title()
            loc = Location(address, postal_code, city, state)
            print(loc_rep.create(loc, session))

        elif loc_choice == 2:
            loc_id = int(input('Enter the location ID to delete:\n'))
            print(loc_rep.delete(loc_id, session))

        elif loc_choice == 3:
            print(loc_rep.select_all(session))

        elif loc_choice == 4:
            find_loc = int(input('1 - Find by ID 2 - Find by name\n'))
            if find_loc == 1:
                loc_id = int(input('Enter the Location ID to find:\n'))
                print(loc_rep.select_one(loc_id, session))

            elif find_loc == 2:
                loc_name = input('Enter the address to find:\n')
                print(loc_rep.select_name(loc_name, session))

        else:
            print('Invalid option, exiting now...')
            break
