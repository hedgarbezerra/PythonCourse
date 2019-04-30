import MySQLdb


def select():
    """O metodo Conn faz a conexão com o banco e faz todas configurações necessárias em caso de erros
    também pensando no caso de SQL injection fechando a conexão após uso"""

    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        #Cursores executam instruções SQL
        cursor.execute("Select department_name from departments")
        """"Existe o Fechone, Fectchmany e Fetchall que funcionam respectivamente retornando o primeiro valor,
        uma quantidade determinada como abaixo e retornando todos os valores retornados pela query\
         Além dos demais existe também o lastrowid"""
        #return cursor.lastrowid

        return cursor.fetchmany(30)
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return 'ERRO:' + str(e).strip('( , )')
    finally:
        database.close()


def insert(dep_id, nome):
    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        database.begin()
        cursor.execute("INSERT INTO departments(department_id, department_name, location_id)"
                       " VALUES ({0}, '{1}', 1700 )".format(dep_id, nome))
        database.commit()
        return 'Os dados foram inseridos com succeso.'
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        database.rollback()
        return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
    finally:
        database.close()


def update(dep_id, nome):
    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        database.begin()
        cursor.execute(
            "UPDATE departments SET department_name = '{1}' WHERE DEPARTMENT_ID = {0}".format(dep_id, nome))
        database.commit()
        return 'O update efetuado com sucesso.'
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        database.rollback()
        return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
    finally:
        database.close()


def delete(dep_id):
    database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306)
    cursor = database.cursor()
    try:
        database.begin()
        cursor.execute("DELETE FROM departments WHERE DEPARTMENT_ID = {0}".format(dep_id))
        database.commit()
        return 'A exclusão foi efetuada com sucesso.'
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        database.rollback()
        return 'ERRO: ' + str(e).strip('( , )') + ' Efetuando rollback'
    finally:
        database.close()


#print(delete(332))
print(update(9999, 'Carlos'))
#print(insert(3342, 'Gourmet'))
#print(select())

