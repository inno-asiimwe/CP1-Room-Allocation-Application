from classes.room import Room, Office,LivingSpace
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


    def create_room(self, use, *names):
        """The method creates one or more  new rooms and returns a list of them"""

        new_rooms = []
        if isinstance(use, str):

            for name in names:
                if not isinstance(name, str):
                    raise TypeError("Name should be string")
                elif name in self.Rooms:
                    raise ValueError("Room  already exists")
                elif use.lower() == 'office':
                        new_room = Office(name)
                        print("A Living space called {} has been successfully created".format(name))
                elif use.lower() == 'livingspace':
                    new_room = LivingSpace(name)
                    print("A Living space called {} has been successfully created".format(name))
                else:
                    raise exception("Type should be office or livingspace")

                self.Rooms.update({new_room.name:new_room})
                new_rooms.append(new_room)

            return new_rooms
        raise TypeError("wrong type")


    def add_person(self, name, role, wants_acommodation = 'n'):
        """Method creates either a staff or fellow object and returns it"""
        exists = False
        if isinstance(name, str) and isinstance(role, str) and (wants_acommodation in ['y', 'Y','n', 'N']):

            if role.lower() == 'staff' or role.lower() == 'fellow':
                new_person = Fellow(name)
                self.allocate_office(new_person)

                if role.lower() == 'fellow' and wants_acommodation.lower() == 'y':
                    #creating a fellow object for the person we are adding, allocate both office and accomodation
                    self.allocate_accomodation(new_person)
                    self.FellowsLivingIn.append(new_person)
                    #add fellow to the list of all fellows
                    self.Fellows.append(new_person)
            else:
                raise ValueError("Role is either staff or fellow")

            return new_person
        raise TypeError("Inputs should be strings")


    def allocate_office(self, person):
        #we randomly pic a room from vacant rooms
        if len(self.OfficesNotFull) > 0:
            index = randint(0,len(self.OfficesNotFull) - 1)
            office = self.OfficesNotFull[index]

            if len(office.occupants) < office.max:
                office.occupants.append(person)
                person.office = office.name
                self.Rooms[office.name] = office

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
            if len(space.occupants) < space.max:

                #allocatig a person a space
                space.occupants.append(person)
                person.Livingspace = space.name
                self.Rooms[space.name] = space
                print("{} has been allocated the office {}".format(person.name, space.name))

                #if a space fills up, move it to the FULL list and remove it from the not full list
                if len(space.occupants) == space.max:
                    self.LivingSpacesFull.append(space)
                    self.LivingSpacesNotFull.remove(space)

    #prints names of all the people in the room
    def print_room(self, room):
        if room in self.Rooms:
            for person in self.Rooms[room].occupants:
                 print(person.name)

    #prints all allocations
    def print_allocations(self, filename = None):
        rooms = self.getAllocatedRooms()

        for room in rooms:
            occupants = room.occupants
            members = []
            for occupant in occupants:
                members.append(occupant.name)
            print(room.name)
            print('---------')
            print(','.join(members))


    def getAllocatedRooms(self):
        allocated = []
        for room in self.Rooms:
            if len(self.Rooms[room].occupants) > 0:
                allocated.append(self.Rooms[room])
        return allocated

    def reallocate(person, room):
        if isinstance(room, Office) and room in self.OfficesNotFull:
            old_office = person.office
            self.Rooms[old_office].occupants.remove(person)
            person.office = self.Rooms[room]
        elif isinstance(room, livingspace) and room in self.LivingSpacesNotFull:
            old_livingspace = person.accomodation


dojo = Dojo()

office1 = dojo.create_room('office', 'Uganda')
office1 = dojo.create_room('livingspace', 'Berlin')
office3 = dojo.create_room('office', 'kenya')
fellow1 = dojo.add_person('peter', 'fellow', 'y')
staff1 = dojo.add_person('inno', 'staff')
print(dojo.Rooms)
dojo.print_allocations()
