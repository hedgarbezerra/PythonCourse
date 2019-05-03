from SQLAlchemy.dominio import db


class ProjectQuery:

    @staticmethod
    def create(project, session):
        session.add(project)

    @staticmethod
    def update(project_id, project, session):
        session.query(db.Project).filter(db.Project.project_id == project_id).update({'project_name': project.project_name,
                                                                                      'manager_id': project.manager_id,
                                                                                      'dt_start': project.dt_start,
                                                                                      'dt_limit': project.dt_limit})

    @staticmethod
    def select_one(project_id, session):
        session.query(db.Project).get(project_id)

    @staticmethod
    def delete(project_id, session):
        session.query(db.Project).filter(db.Project.project_id == project_id).delete()
