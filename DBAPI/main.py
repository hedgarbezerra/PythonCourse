from DBAPI.Department import Department
from DBAPI.DeptConnection import DepConnection


if __name__ == '__main__':
    #dep = Department(144, 'Novo nome', None, 1700)
    Con = DepConnection()
    Con.departament = Department(144, 'Novo ', None, 1700)
    #print(Con.delete())
    #print(Con.insert())
    #print(Con.update())
    print(Con.select())
