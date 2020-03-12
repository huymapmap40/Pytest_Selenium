
class Customer:

    def __init__(self, name, birth_date, address, city, state, pin, mobile_number, email, password):
        self._name = name
        self._birth_date = birth_date
        self._address = address
        self._city = city
        self._state = state
        self._pin = pin
        self._mobile_number = mobile_number
        self._email = email
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        self._pin = value

    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
