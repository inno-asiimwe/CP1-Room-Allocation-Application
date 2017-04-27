from classes.room import Room, Office,LivingSpace
from classes.person import Fellow, Staff, Person
import random

class Dojo:

    def __init__(self):
        self.Rooms = {}
        self.Persons = []
        self.offices = []
        self.livingspaces = []



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
                        self.offices.append(new_room)
                        print("A Living space called {} has been successfully created".format(name))
                elif use.lower() == 'livingspace':
                    new_room = LivingSpace(name)
                    self.livingspaces.append(new_room)
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
                    #add fellow to the list of all fellows

            else:
                raise ValueError("Role is either staff or fellow")

            self.Persons.append(new_person)
            return new_person
        raise TypeError("Inputs should be strings")


    def allocate_office(self, person):
        """method randomily allocates an office to fellow or staff"""
        #randomly picking an office from available offices
        available = self.find_available(self.offices)
        if len(available) > 0:
            office = random.choice(available)
            #assigning the office to the person
            office.occupants.append(person)
            person.office = office.name
            #updating the dictionary Rooms with new Value
            self.Rooms[office.name] = office
            print("{} has been allocated the Living space {}".format(person.role, person.name, office.name))
        else:
            print("Not office allocated for {}".format(person.name))


    def allocate_accomodation(self, person):
        """method randomly allocates an living spaces"""
        #randomly picking a space
        available = self.find_available(self.livingspaces)

        if len(available):
            space = random.choice(available)
            #assigning the space to the person
            space.occupants.append(person)
            person.accomodation = space.name
            #updating the dictionary
            self.Rooms[space.name] = space
            print("{} has been allocated the Living space {}".format(person.role, person.name, space.name))
        else:
            print("No living space allocated for {}".format(person.name))

    def find_available(self, alist):
        """method returns a list of available offices or living spaces"""
        new_list = []

        for member in alist:
            if len(member.occupants) < member.max:
                new_list.append(member)
        return new_list

    #prints names of all the people in the room
    def print_room(self, room):
        """method to print names of all people in a room"""""
        if room in self.Rooms:
            for person in self.Rooms[room].occupants:
                 print(person.name)

    #prints all allocations
    def print_allocations(self, filename = None):
        """prints names of people in each room"""
        allocations = self.get_allocations()
        self.list_to_print(allocations, filename)


    def get_allocated_rooms(self):
        allocated = []
        for room in self.Rooms:
            if len(self.Rooms[room].occupants) > 0:
                allocated.append(self.Rooms[room])
        return allocated

    def get_allocations(self):
        separator ='-------------------'
        rooms = self.get_allocated_rooms()
        prints = []
        for room in rooms:
            occupants = room.occupants
            members = []
            for occupant in occupants:
                members.append(occupant.name)
            memberstostring = ','.join(members)
            print_string = room.name + '\n' + separator + '\n' + memberstostring + '\n'
            prints.append(print_string)
        return prints

    def list_to_print(self, alist, filename = None):
        for item in alist:
            if(filename != None):
                with open(filename, 'a')as f:
                    f.write(item)
            else:
                print(item)

        def print_unallocated(self):
            pass


dojo = Dojo()
office1 = dojo.create_room('office', 'Uganda')
office1 = dojo.create_room('livingspace', 'Berlin')
office3 = dojo.create_room('office', 'kenya')
fellow1 = dojo.add_person('peter', 'fellow', 'y')
staff1 = dojo.add_person('inno', 'staff')
print(dojo.Rooms)
dojo.print_allocations('example')
