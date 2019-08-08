import unittest
from city_functions import city_country

class Test_test_cites(unittest.TestCase):
    """ Test dla programu city_functions.py """
    
    def test_city_country(self):
        answer = city_country('warszawa', 'polska')
        self.assertEqual(answer, "Warszawa, Polska")

    def test_city_country_population(self):
        """ W teście dodano 'population' """
        answer = city_country('moskwa', 'federacja rosyjska', 127000000)
        self.assertEqual(answer, "Moskwa, Federacja Rosyjska, populacja: 127000000")

if __name__ == '__main__':
    unittest.main()
