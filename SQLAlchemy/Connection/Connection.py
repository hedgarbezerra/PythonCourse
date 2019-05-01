import MySQLdb
import configparser
from sqlalchemy import create_engine


class Connection:

    @staticmethod
    def connect():
        config = configparser.ConfigParser()
        config.read('C:/Users/wsm/PycharmProjects/PythonCourse/config.ini')
        user = config['DATABASE']['user']
        passwd = config['DATABASE']['passwd']
        db = config['DATABASE']['db']
        host = config['DATABASE']['host']
        port = int(config['DATABASE']['port'])

        database = create_engine(f'mysql://{user}:{passwd}@{host}:{port}/{db}')
        return database
