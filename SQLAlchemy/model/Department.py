class Department:
    def __init__(self, department_id, department_name, manager_id=None, location_id=None):
        self.__department_id = department_id
        self.__department_name = department_name
        self.__manager_id = manager_id
        self.__location_id = location_id

    @property
    def id(self):
        return self.__department_id

    @id.setter
    def id(self, value):
        self.__department_id = value

    @property
    def name(self):
        return self.__department_name

    @name.setter
    def name(self, value):
        self.__department_name = value

    @property
    def manager(self):
        return self.__manager_id

    @manager.setter
    def manager(self, value):
        self.__manager_id = value

    @property
    def location(self):
        return self.__location_id

    @location.setter
    def location(self, value):
        self.__location_id = value


