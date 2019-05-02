from Kivy.Repository.DeptConnection import DepConnection
from Kivy.model.Department import Department


if __name__ == '__main__':
    dep = Department(991, 'Macaco', 101, 1700)
    Con = DepConnection()
    Con.departament = dep
    Con.insert()
    print(Con.select())


