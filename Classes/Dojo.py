from classes.room import Room,Office
class Dojo:

    def __init__(self):
        self.Rooms = []
        self.Persons = []
        self.Offices = []
        self.LivingSpaces = []
        self.Fellows = []
        self.Staff = []
        self.VacantRooms = []
        self.NewRooms = []
        self.FullRooms = []
        self.FellowsLivingIn = []


    def create_room(self, typ, *names):

        if isinstance(typ, str):
            new_rooms = []

            for name in names:
                if not isinstance(name, str):
                    raise TypeError("Name should be string")

                else:

                    for room in self.Rooms:
                        if name == room.name:
                            raise ValueError("Room  already exists")

                    if typ.lower() == 'office':
                        new_room = Office(name)
                        self.Offices.append(new_room)
                        self.Rooms.append(new_room)
                        new_rooms.append(new_room)

                    if typ.lower() == 'livingspace':
                        new_room = LivingSpace(name)
                        self.offices.append(new_room)
                        self.Rooms.append(new_room)

                
            return new_rooms

        raise TypeError("wrong type")
            # if typ.lower() != 'office' or typ.strip().lower() != 'livingspace':
            #     raise ValueError("type should be office or Living space");
