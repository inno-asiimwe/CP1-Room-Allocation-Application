from classes.room import Room,Office
from classes.person import Fellow, Staff
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
                        print("An Office called {} has been successfully created".format(name))

                    if typ.lower() == 'livingspace':
                        new_room = LivingSpace(name)
                        self.offices.append(new_room)
                        self.Rooms.append(new_room)
                        new_rooms.append(new_room)
                        print("A Living space called {} has been successfully created".format(name))


            return new_rooms

        raise TypeError("wrong type")
            # if typ.lower() != 'office' or typ.strip().lower() != 'livingspace':
            #     raise ValueError("type should be office or Living space");
    #
    def add_person(self, name, role, wants_acommodation):
        if role == 'staff' or role == 'fellow':
            if role.lower() == 'fellow' and wants_acommodation.lower() == 'y':
                #creating a fellow object for the person we are adding, allocate both office and accomodation
                new_person = Fellow(name)
                new_person.allocate_office()
                new_person.allocate_accomodation()
                #add fellow to the list of all fellows
                self.Fellows.append(new_person)
            #if fellow opted out of accomodation only allocate office space and append fellow to the list of all fellows
            if role.lower() =='fellow' and wants_acommodation == 'n':
                new_person = Fellow(name)
                new_person.allocate_office()
                self.Fellows.append(new_person)
            #making sure that fellow must always opt in or out of accomodation
            if role.lower() == 'fellow' and (wants_acommodation == None or wants_acommodation == ''):
                raise(ValueError("Fellow should either opt in or out for accomodation"))

            if role.lower() == 'staff':
                new_person = Staff(name)
                new_person.allocate_office()
                self.Staff.append(new_person)







        raise(ValueError)
