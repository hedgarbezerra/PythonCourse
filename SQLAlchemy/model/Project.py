class Project:

    def __init__(self, name, manager_id, dt_limit, dt_start=None, project_id=None):
        self.__project_id = project_id
        self.__name = name
        self.__manager_id = manager_id
        self.__dt_start = dt_start
        self.__dt_limit = dt_limit

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, value):
        self.__project_id = value

    @property
    def project_name(self):
        return self.__name

    @project_name.setter
    def project_name(self, value):
        self.__name = value

    @property
    def manager_id(self):
        return self.__manager_id

    @manager_id.setter
    def manager_id(self, value):
        self.__manager_id = value

    @property
    def dt_start(self):
        return self.__dt_start

    @dt_start.setter
    def dt_start(self, value):
        self.__dt_start = value

    @property
    def dt_limit(self):
        return self.__dt_limit

    @dt_limit.setter
    def dt_limit(self, value):
        self.__dt_limit = value

    def __repr__(self):
        return f'Project #{self.__project_id} - {self.__name} //' \
            f' Project through {self.__dt_start} ~ {self.__dt_limit}\n'
