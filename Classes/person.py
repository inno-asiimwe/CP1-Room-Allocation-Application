class Person:
    def __init__(self, role, name):
        self.role = role
        self.name = name
        self.office = None

class Staff(Person):
    def __init__(self, name):
        Person.__init__(self, 'staff', name)


class Fellow(Person):
    def __init__(self, name):
        Person.__init__(self,'fellow', name)
