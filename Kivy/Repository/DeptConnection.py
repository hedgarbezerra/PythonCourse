import MySQLdb
from MySQLdb.compat import unicode
from DBAPI.Connection import Connection
from DBAPI.Department import Department


class DepConnection:
    def __init__(self):
        department = Department()

    def select(self):
        try:
            database = Connection.connect()
            cursor = database.cursor()
            cursor.execute("Select d.department_id, d.department_name, concat(e.first_name,' ', e.LAST_NAME),"
                                " d.LOCATION_ID from departments d left join employees e on d.MANAGER_ID = EMPLOYEE_ID "
                                "where d.DEPARTMENT_ID = {0}".format(self.__department.id))
            return cursor.fetchall()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            return 'ERRO:' + str(e).strip('( , )')
        finally:
            database.close()

    def insert(self):
        database = Connection.connect()
        cursor = database.cursor()
        try:
            database.begin()
            cursor.execute("INSERT INTO departments(department_id, department_name, location_id)"
                           " VALUES ({0}, '{1}', 1700 )".format(self.__department.id, self.__department.name))
            database.commit()
            return 'Os dados foram inseridos com succeso.'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            database.rollback()
            return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
        finally:
            database.close()

    def update(self):
        database = Connection.connect()
        cursor = database.cursor()
        try:
            database.begin()
            cursor.execute(
                "UPDATE departments SET department_name = '{1}' WHERE DEPARTMENT_ID = {0}".format(
                    self.__department.id, self.__department.name))
            database.commit()
            return 'O update efetuado com sucesso.'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            database.rollback()
            return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
        finally:
            database.close()

    def delete(self):
        database = Connection.connect()
        cursor = database.cursor()
        try:
            database.begin()
            cursor.execute("DELETE FROM departments WHERE DEPARTMENT_ID = {0}".format(
                self.__department.id
            ))
            database.commit()
            return 'A exclusão foi efetuada com sucesso.'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            database.rollback()
            return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
        finally:
            database.close()

    @property
    def departament(self):
        return self.__department

    @departament.setter
    def departament(self, value):
        self.__department = value
