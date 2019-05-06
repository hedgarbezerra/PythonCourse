from SQLAlchemy.Connection import db


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
        project = session.query(db.Project).get(project_id)
        return project

    @staticmethod
    def delete(project_id, session):
        session.query(db.Project).filter(db.Project.project_id == project_id).delete()

    @staticmethod
    def select_all(session):
        projects = session.query(db.Project).all()
        return projects

    @staticmethod
    def select_name(project_name, session):
        projects = session.query(db.Project).filter(db.Project.project_name == project_name).all()
        return projects
