import unittest
from employee import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        print("Setup has been run")
        self.stud_1 = Student('as', 'ak', 300)
        self.stud_2 = Student('novak', 'onkundi', 300)
        self.parent_name = "Barrack Obama"

    def tearDown(self):
        print("teardown has been run")
    

    def test_email(self):

        self.assertEqual(self.stud_1.email, 'as.ak@gmail.com')
        self.assertEqual(self.stud_2.email, "novak.onkundi@gmail.com")

    def test_fullname(self):
        self.assertEqual(self.stud_1.fullname, "kelvin onkundi")

        