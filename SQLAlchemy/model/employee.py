class Employee:
    def __init__(self, employee_id, name, email, phone=None, job=None, salary=None):
        self.__employee_id = employee_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__job = job
        self.__salary = salary

    @property
    def id(self):
        return self.__employee_id

    @id.setter
    def id(self, value):
        self.__employee_id  = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        self.__job = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

