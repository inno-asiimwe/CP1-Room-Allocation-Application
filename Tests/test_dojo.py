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

    def test_room_is_does_not_exist_yet(self):
        """The room should not be in the system as yet"""
        new_room = self.dojo.create_room('office', 'Germany')
        self.assertRaises(ValueError, self.dojo.create_room, 'office', 'Germany')


    def test_room_created_has_intended_attributes(self):
        """The room created should be either office or living space"""
        new_room = self.dojo.create_room('office', 'Germany')
        self.assertTrue([new_room[0].typ, new_room[0].name] == ['office', 'Germany'])

    def test_room_created_only_accepts_strings(self):
        """Input both inputs should be strings """
        self.assertRaises(TypeError, self.dojo.create_room, 5, 2)
        self.assertRaises(TypeError, self.dojo.create_room, 'office', 7)
        self.assertRaises(TypeError, self.dojo.create_room, 8, '')

    # def test_create_room_only_accepts_type_office_living(self):
    #     """The type argument should accept only office and livingspace"""
    #     self.assertRaises(ValueError, self.dojo.create_room, 'bedroom', 'Germany')



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
    #
    #
    # # def test_person_is_fellow_or_staff(self):
    # #     """Person created must be either an instance of fellow or staff"""
    # #     new_person1 = dojo.createPerson('patrick', 'fellow', 'y')
    # #     new_person2 = dojo.createPerson('john', 'staff')
    # #
    # #     assertTrue(IsInstance(new_person1, Fellow) == IsInstance(new_person2, Staff))
    #
    #
    def test_add_person_raises_typeerror_for_nonstrings(self):
        """arguments must be strings"""
        self.assertRaises(TypeError, self.dojo.add_person, 78, 'fellow', 'y')
    # #
    # #
    # # def test_add_person_raises_valueerror_for_type_not_staff_or_fellow(self):
    # #     """type argument should only be staff or fellow"""
    # #     self.assertRaises(ValueError("type must be staff or Fellow"), add_person, )
    # #
    # #
    # # def test_raises_value_error_for_staff_livingin(self):
    # #     """Staff can not opt to leave in"""

    @mock.patch('builtins.print')
    def test_print_room_success(self, fake_print):
        room1 = self.dojo.create_room('office', 'Germany')
        new_person = self.dojo.add_person('patrick', 'staff')
        self.dojo.print_room('Germany')
        fake_print.assert_called_with('patrick')

    # def test_print_allocation_success(self):
    #     pass




if __name__ == '__main__':
    unittest.main()
