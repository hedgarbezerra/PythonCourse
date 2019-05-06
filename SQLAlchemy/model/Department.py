class Department:
    def __init__(self, department_name, manager_id=None, location_id=None, department_id=None):
        self.__department_id = department_id
        self.__department_name = department_name
        self.__manager_id = manager_id
        self.__location_id = location_id

    @property
    def department_id(self):
        return self.__department_id

    @department_id.setter
    def department_id(self, value):
        self.__department_id = value

    @property
    def department_name(self):
        return self.__department_name

    @department_name.setter
    def department_name(self, value):
        self.__department_name = value

    @property
    def manager_id(self):
        return self.__manager_id

    @manager_id.setter
    def manager(self, value):
        self.__manager_id = value

    @property
    def location_id(self):
        return self.__location_id

    @location_id.setter
    def location_id(self, value):
        self.__location_id = value

    def __repr__(self):
        return f"Departmente #{self.department_id} nomeado: {self.department_name}\n"
