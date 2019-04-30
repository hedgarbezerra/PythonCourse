import MySQLdb


def update(dep_id, nome):
    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        database.begin()
        cursor.execute("UPDATE departments SET department_name = '{1}' WHERE DEPARTMENT_ID = {0}".format(dep_id, nome))
        database.commit()
        return 'O update efetuado com sucesso.'
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        database.rollback()
        return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
    finally:
        database.close()


def insert(tuples):
    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        database.begin()
        cursor.executemany("INSERT INTO departments(department_id, department_name, location_id)"
                       " VALUES (%s, %s, 1700)", tuples)
        database.commit()
        return 'Os dados foram inseridos com succeso.'
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        database.rollback()
        return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
    finally:
        database.close()


tuples1 = ((111, 'TI coroi'), (122, 'Outra'), (133, 'Mais uma'), (144, 'Final'))
print(insert(tuples1))
nome1 = "Carlos, locn_id = 17"
#print(update(300, nome1))
