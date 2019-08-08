import unittest

from Tests import Employee

class Test_test_Employee(unittest.TestCase):
    """Testy dla klasy Employee """

    def setUp(self):
        """Utorzenie zestawu testowego dla wszystkich testów
           dla klasy Employee.
        """
        self.my_employee = Employee('John', 'Doe', 1000)

    def test_give_default_rise(self):
        """Domyślne zwiększenie uposażenia o 5000 zł"""
        self.my_employee.give_raise()
        self.assertEqual(6000, self.my_employee.wynagrodzenie)

    def test_give_custom_raise(self):
        """Zwiększenie uposażenia o konkretną kwotę = 1000 zł"""
        self.my_employee.give_raise(1000)
        self.assertEqual(2000, self.my_employee.wynagrodzenie)

if __name__ == '__main__':
    unittest.main()
