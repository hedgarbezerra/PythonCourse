import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Project_query import ProjectQuery
from SQLAlchemy.dominio.db import Project


class ProjectRep:

    @staticmethod
    def select(project_id, session):
        query = ProjectQuery()
        try:
            query.select(project_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def create(project, session):
        query = ProjectQuery()
        project = Project(project_name=project.project_name , dt_start=project.dt_start,
                          dt_limit=project.dt_limit, manager_id=project.manager_id)
        try:
            query.create(project, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Project registered sucessfully!'
        finally:
            session.close()

    @staticmethod
    def update(project_id, project, session):
        query = ProjectQuery()
        try:
            query.update(project_id, project, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Project sucessfully updated!'
        finally:
            session.close()

    @staticmethod
    def delete(project_id, session):
        query = ProjectQuery()
        try:
            query.delete(project_id, session)
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            session.rollback()
            return 'ERRO: ' + str(e).strip('( , )')
        else:
            session.commit()
            return 'Project sucessfully deleted!'
        finally:
            session.close()

