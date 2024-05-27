import unittest
from lib.teacher import Teacher

class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.my_teacher = Teacher("My", "Teacher")

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        from lib.user import User
        self.assertTrue(issubclass(Teacher, User))

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        self.assertEqual((self.my_teacher.first_name, self.my_teacher.last_name), ("My", "Teacher"))

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        self.assertIsInstance(self.my_teacher.knowledge, list)
        self.assertGreater(len(self.my_teacher.knowledge), 0)

    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        self.assertIn(self.my_teacher.teach(), self.my_teacher.knowledge)

if __name__ == '__main__':
    unittest.main()
