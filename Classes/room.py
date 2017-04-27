class Room:
    def __init__(self, typ, name,max):
        self.typ = typ
        self.name = name
        self.max = max
        self.occupants = []


class Office(Room):
    def __init__(self, name):
        super(Office, self).__init__('office', name, 6)
        # self.name = name
        # self.max = 4
        # self.typ = 'office'


class LivingSpace(Room):
    def __init__(self, name):
        super(LivingSpace, self).__init__('livingspace', name, 4)
