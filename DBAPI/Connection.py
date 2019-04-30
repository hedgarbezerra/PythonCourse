import MySQLdb
import configparser


class Connection:

    @staticmethod
    def connect():
        config = configparser.ConfigParser()
        config.read('C:/config.ini')
        database = MySQLdb.connect(user=config['DATABASE']['user'],
                                   db=config['DATABASE']['db'],
                                   host=config['DATABASE']['host'],
                                   port=int(config['DATABASE']['port']),
                                   charset=config['DATABASE']['charset'],
                                   autocommit=config['DATABASE']['autocommit'])
        return database

    @staticmethod
    def cursor():
        database = MySQLdb.connect(user="root", db="tw_nfe", host="localhost", port=3306, charset='utf8')
        cursor = database.cursor()
        return cursor
