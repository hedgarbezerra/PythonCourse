class EmpProj:
    def __init__(self, employee_id, project_id):
        self.__employee_id = employee_id
        self.__project_id = project_id

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def project_id(self):
        return self.__project_id
