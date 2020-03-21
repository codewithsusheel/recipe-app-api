from django.tests import TestCase

from app.calc import add

class CalcTests(TestCase):

    def test_Add_numbers(self):
        self.assertEqual(add(3, 8), 11)