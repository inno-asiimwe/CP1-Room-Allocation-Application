class Person:
    def __init__(self, role, name, office = None, accomodation = None):
        self.role = role
        self.name = name
        self.office = offices
        self.accomodation = accomodation

class Staff(Person):
    def __init__(self, name):
        Person.__init__(self, 'staff', name)


class Fellow(Person):
    def __init__(self, name):
        Person.__init__(self,'fellow', name)
