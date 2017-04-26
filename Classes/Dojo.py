from classes.room import Room, Office, LivingSpaces
from classes.person import Fellow, Staff, Person
from random import randint

class Dojo:

    def __init__(self):
        self.Rooms = {}
        self.Persons = []
        self.Offices = []
        self.LivingSpaces = []
        self.LivingSpacesFull = []
        self.LivingSpacesNotFull = []
        self.Fellows = []
        self.Staff = []
        self.VacantRooms = []
        self.NewRooms = []
        self.OfficesFull = []
        self.OfficesNotFull = []
        self.FullRooms = []
        self.FellowsLivingIn = []
        self.FellowsLivingOut = []


    def create_room(self, typ, *names):

        if isinstance(typ, str):
            new_rooms = []

            for name in names:
                if not isinstance(name, str):
                    raise TypeError("Name should be string")

                else:

                    if name in self.Rooms:
                            raise ValueError("Room  already exists")

                    if typ.lower() == 'office':
                        new_room = Office(name)
                        self.OfficesNotFull.append(new_room)
                        self.Offices.append(new_room)
                        self.Rooms.update({new_room.name:new_room})
                        new_rooms.append(new_room)
                        print("An Office called {} has been successfully created".format(name))

                    if typ.lower() == 'livingspace':
                        new_room = LivingSpace(name)
                        self.LivingSpacesNotFull.append(new_room)
                        self.LivingSpaces.append(new_room)
                        self.Rooms.update({new_room.name:new_room})
                        new_rooms.append(new_room)
                        print("A Living space called {} has been successfully created".format(name))


            return new_rooms

        raise TypeError("wrong type")
            # if typ.lower() != 'office' or typ.strip().lower() != 'livingspace':
            #     raise ValueError("type should be office or Living space");

    def add_person(self, name, role, wants_acommodation = 'n'):
        exists = False
        if isinstance(name, str) and isinstance(role, str) and (wants_acommodation in ['y', 'Y','n', 'N']):

            for person in self.Persons:
                if name == person.name:
                    exists = True

            if exists:
                raise ValueError("Person already exists")
            else:
                if role == 'staff' or role == 'fellow':

                    if role.lower() == 'fellow' and wants_acommodation.lower() == 'y':
                        #creating a fellow object for the person we are adding, allocate both office and accomodation
                        new_person = Fellow(name)
                        self.Persons.append(new_person)
                        self.allocate_office(new_person)
                        self.allocate_accomodation(new_person)
                        #add fellow to the list of all fellows
                        self.Fellows.append(new_person)
                    #if fellow opted out of accomodation only allocate office space and append fellow to the list of all fellows
                    if role.lower() =='fellow' and wants_acommodation == 'n':
                        new_person = Fellow(name)
                        self.Persons.append(new_person)
                        self.allocate_office(new_person)
                        self.Fellows.append(new_person)
                    #making sure that fellow must always opt in or out of accomodation
                    if role.lower() == 'fellow' and (wants_acommodation == None or wants_acommodation == ''):
                        raise ValueError("Fellow should either opt in or out for accomodation")

                    if role.lower() == 'staff':
                        new_person = Staff(name)
                        self.Persons.append(new_person)
                        print()
                        self.allocate_office(new_person)
                        self.Staff.append(new_person)
                else:
                    raise ValueError("Role is either staff or fellow")
            return new_person
        raise TypeError("Inputs should be strings")


    def allocate_office(self, person):
        #we randomly pic a room from vacant rooms
        if len(self.OfficesNotFull) > 0:
            index = randint(0,len(self.OfficesNotFull) - 1)
            office = self.OfficesNotFull[index]

            while len(office.occupants) < office.max:
                office.occupants.append(person)
                person.office = office.name
                self.Rooms[office.name] = Office

                if len(office.occupants) == office.max:
                    self.OfficesFull.append(office)
                    self.OfficesNotFull.remove(office)
        #raise RuntimeError("There are no offices to allocate")


    def allocate_accomodation(self, person):
        #randomly choosing an index of a space

        if len(self.LivingSpacesNotFull) > 0:
            index = randint(0,len(self.LivingSpacesNotFull) - 1)
            space = self.LivingSpacesNotFull[index]

            #making sure the space is not full
            while len(space.occupants) < space.max:

                #allocatig a person a space
                space.occupants.append(person)
                person.Livingspace = space.name
                self.Rooms[space.name] = space
                print("{} has been allocated the office {}".format(person.name, space.name))

                #if a space fills up, move it to the FULL list and remove it from the not full list
                if len(space.occupants) == space.max:
                    LivingSpacesFull.append(space)
                    LivingSpacesNotFull.remove(space)


    def print_room(self, room):
        print(self.Rooms[room])
