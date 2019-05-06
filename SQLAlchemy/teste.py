import json
from SQLAlchemy.repositorio import Employee_Rep, Location_Rep, Department_Rep, Project_Rep
from SQLAlchemy.Connection import Connection, db
from SQLAlchemy.endereco import Endereco
import requests
import pprint
from SQLAlchemy.model.Project import Project


s = 10
e = 20

while s < e:
    s += 1
    sqrt = s**0.5
    print(f'{sqrt}.3f')

"""
session = Connection.Connection().session()
session.query()
emp_rep = Employee_Rep.EmployeeRep()
dep = Department_Rep.DepartmentRep()
proj = Project('Final Sprint', 2, dt_limit='2019-08-20')
projd = Project_Rep.ProjectRep()
loc = Location_Rep.LocationRep()



# print(projd.create(proj, session))
#print(emp_rep.select_cpf(''))
# .filter(db.Employee.name == 'Zeus').one_or_none())

locations = loc.obj_list(session)
employees = emp_rep.obj_list(session)
departaments = dep.obj_list(session)
projects = projd.obj_list(session)
print(employees)

for i in projd.select_all(session):
    project = Project(project_id=i.project_id, name=i.project_name, manager_id=i.manager_id,
                      dt_start=i.dt_start, dt_limit=i.dt_limit)
    dic.append(project)

print(dic[0])
projeto = dic[1]
print(projeto.project_id)
print(projeto)

for i in projd.select_all(session):
    dic[i.project_id] = {'#ID': i.project_id, 'Name': i.project_name, 'Start': str(i.dt_start), 'Ends': str(i. dt_limit)}
pprint.pprint(dic)
"""
