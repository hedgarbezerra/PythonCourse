import MySQLdb
from sqlalchemy import exc
from SQLAlchemy.Connection.Project_query import ProjectQuery
from SQLAlchemy.Connection.db import Project
from SQLAlchemy.repositorio.Employee_Rep import EmployeeRep


class ProjectRep:

    @staticmethod
    def create(project, session):
        query = ProjectQuery()
        emp_rep = EmployeeRep()
        employee = emp_rep.select_one(project.manager_id, session)
        project = Project(project_name=project.project_name, dt_start=project.dt_start,
                          dt_limit=project.dt_limit, manager_id=project.manager_id, employee=employee)
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

    @staticmethod
    def select_one(project_id, session):
        query = ProjectQuery()
        try:
            project = query.select_one(project_id, session)
            return project
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_all(session):
        query = ProjectQuery()
        try:
            projects = query.select_all(session)
            return projects
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    @staticmethod
    def select_name(project_name, session):
        query = ProjectQuery()
        try:
            projects = query.select_name(project_name, session)
            return projects
        except (exc.SQLAlchemyError, exc.DBAPIError, MySQLdb.Error, exc.DatabaseError, MySQLdb.DatabaseError) as e:
            return 'ERRO: ' + str(e).strip('( , )')
        finally:
            session.close()

    def obj_list(self, session):
        projects = []
        for obj in self.select_all(session):
            project = Project(project_id=obj.project_id, project_name=obj.project_name, manager_id=obj.manager_id,
                              dt_start=obj.dt_start, dt_limit=obj.dt_limit)
            projects.append(project)
        return projects
