class Room:
    def __init__(self, typ, name,max):
        self.typ = typ
        self.name = name
        self.max = max
        self.occupants = []


class Office:
    def __init__(self, name):
        Room.__init__(self, 'office', name, 6)


class LivingSpace:
    def __init__(self, name):
        Room.__init__(self, 'livingspace', name, 4)
