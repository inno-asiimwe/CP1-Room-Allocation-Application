class Room:
    def __init__(self, name, typ):
        self.typ = typ
        self.name = name

class Office:
    def __init__(self, name):
        Room.__init__(self, name, typ = 'office')


class LivingSpace:
    def __init__(self, name):
        Room.__init__(self,name, typ = 'livingspace')
