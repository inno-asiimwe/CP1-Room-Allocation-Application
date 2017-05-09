class Room:
    def __init__(self, use, name, max, occupants = [] ):
        self.use = use
        self.name = name
        self.max = max
        self.occupants = occupants


class Office(Room):
    def __init__(self, name):
        super(Office, self).__init__('office', name, 6)



class LivingSpace(Room):
    def __init__(self, name):
        super(LivingSpace, self).__init__('livingspace', name, 4)
