import unittest
from classes.Dojo import Dojo
from unittest import mock

class TestDojo(unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_success(self):
        """Testing a room was successfully created"""
        before_count = len(self.dojo.Rooms)
        new_room = self.dojo.create_room('office', 'German', 'Uganda', 'Benin')
        after_count = len(self.dojo.Rooms)
        self.assertEqual(before_count + len(['German', 'Uganda', 'Benin']), after_count )

    def test_room_does_not_exist_yet(self):
        """The room should not be in the system as yet"""
        new_room = self.dojo.create_room('office', 'Germany')
        self.assertRaises(ValueError, self.dojo.create_room, 'office', 'Germany')


    def test_room_created_only_accepts_strings(self):
        """Input both inputs should be strings """
        self.assertRaises(TypeError, self.dojo.create_room, 5, 2)
        self.assertRaises(TypeError, self.dojo.create_room, 'office', 7)
        self.assertRaises(TypeError, self.dojo.create_room, 8, '')

    def test_add_person_success(self):
        """A person should be added to"""
        before_count = len(self.dojo.Persons)
        new_person = self.dojo.add_person('patrick', 'fellow', 'y')
        after_count = len(self.dojo.Persons)
        self.assertEqual(before_count + 1, after_count)

    def test_person_is_not_already_added(self):
        """Person can be only added once"""
        new_person1 = self.dojo.add_person('patrick', 'fellow', 'y')
        self.assertRaises(ValueError, self.dojo.add_person, 'patrick','fellow','y')

    def test_person_added_has_intended_attributes(self):
        new_person = self.dojo.add_person('patrick', 'fellow', 'y')
        self.assertEqual([new_person.name, new_person.role], ['patrick', 'fellow'])

    def test_add_person_raises_typeerror_for_nonstrings(self):
        """arguments must be strings"""
        self.assertRaises(TypeError, self.dojo.add_person, 78, 'fellow', 'y')

    @mock.patch('builtins.print')
    def test_print_room_success(self, fake_print):
        """should print occupants of the room"""
        self.dojo.create_room('office', 'Germany')
        new_person = self.dojo.add_person('patrick', 'staff')
        self.dojo.print_room('Germany')
        fake_print.assert_called_with('patrick')

    @mock.patch('builtins.print')
    def test_print_allocation_success(self, fake_print):
        """should print occupants per room"""
        self.dojo.create_room('office', 'Germany')
        new_person = self.dojo.add_person('patrick', 'staff')
        self.dojo.print_allocations()
        fake_print.assert_called_with('Germany')
        fake_print.assert_called_with('----'*3)
        fake_print.assert_called_with('patrick')

    @mock.patch('builtins.print')
    def test_print_unallocated(self, fake_print):
        """All are allocated offices, all staff are not allocated Livigspaces,
        Some Fellows opt out of being allocated livingspaces"""
        self.dojo.create_room('office', 'Germany', 'Brazil', 'Nigeria')
        self.dojo.create_room('Livingspace', 'Nairobi')
        staff1 = self.dojo.add_person('Innocent', 'staff')
        fellow1 = self.dojo.add_person('Asiimwe', 'fellow' 'y')
        fellow2 = self.dojo.add_person('Sheila', 'fellow' 'n')
        fake_print.assert_called_with('Innocent')
        fake_print.assert_called_with('Sheila')






if __name__ == '__main__':
    unittest.main()
