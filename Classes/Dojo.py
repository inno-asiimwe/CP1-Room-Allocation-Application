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

            #checking if a person already exists and raise an exception in case person exists
            for person in self.Persons:
                if name == person.name:
                    exists = True

            if exists:
                raise ValueError("Person already exists")
            else:
                if role.lower() == 'staff' or role.lower() == 'fellow':

                    if role.lower() == 'fellow' and wants_acommodation.lower() == 'y':
                        #creating a fellow object for the person we are adding, allocate both office and accomodation
                        new_person = Fellow(name)
                        self.Persons.append(new_person)
                        self.allocate_office(new_person)
                        self.allocate_accomodation(new_person)
                        self.FellowsLivingIn.append(new_person)
                        #add fellow to the list of all fellows
                        self.Fellows.append(new_person)

                    #if fellow opted out of accomodation only allocate office space and append fellow to the list of all fellows
                    if role.lower() =='fellow' and wants_acommodation == 'n':
                        new_person = Fellow(name)
                        self.Persons.append(new_person)
                        self.allocate_office(new_person)
                        self.Fellows.append(new_person)
                        self.FellowsLivingOut(new_person)

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

            if (office.occupants) < office.max:
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

            #     """
            # if filename:
            #     with Open(filename, 'w')as f:
            #         f.write(room.name)
            #         f.write('-----------')
            #         f.write(','.join(names))
            #
            #
            # else:
            #         print(room.name)
            #         print('---------------')
            #         print(','.join(names))


        # word = []
        # if filename:
        #     with Open(filename, 'w') as f:
        #         for key,value in self.Rooms.items():
        #             if len(value.occupants) > 0:
        #                 f.write(key)
        #                 f.write('---'*4 +"\n")
        #                 for occupant in value.occupants:
        #                     word.append(occupant.name)
        #                 f.write(','.join(word))
        # else:
        #     for key, value in self.Rooms.items():
        #         if len(value.occupants) > 0:
        #             print(key)
        #             # print('---'*4)
        #             # for occupant in value.occupants:
        #             #     word.append(occupant.name)
        #             # print(','.join(word))

    #printing all the unallocated persons
    def print_unallocated(self, filename = None):
        if filename:
            with Open(filename, 'w') as f:
                for member in self.Staff:
                    f.write(member.name)

                for fellow in FellowsLivingOut:
                    f.write(fellow.name)

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
print(staff1.name)
dojo.print_allocations()
#print(dojo.Rooms['Uganda'].name)
#dojo.print_allocations()
#print(dojo.Rooms['uganda'])
