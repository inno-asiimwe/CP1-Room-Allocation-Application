class Room:
    def __init__(self, typ, name):
        self.typ = typ
        self.name = name

class Office:
    def __init__(self, name):
        Room.__init__(self, 'office', name)


class LivingSpace:
    def __init__(self, name):
        Room.__init__(self, 'livingspace', name,)
