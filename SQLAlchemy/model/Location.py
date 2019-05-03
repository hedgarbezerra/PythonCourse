class Location:
    def __init__(self, address, postal_code, city, state):
        self.__location_id = None
        self.__address = address
        self.__postal_code = postal_code
        self.__city = city
        self.__state = state

    @property
    def location_id(self):
        return self.__location_id

    @location_id.setter
    def location_id(self, value):
        self.__location_id = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def postal_code(self):
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, value):
        self.__postal_code = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

