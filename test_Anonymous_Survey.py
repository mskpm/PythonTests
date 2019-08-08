import unittest

from Survey import AnonymousSurvey

class Test_TestAnonymousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey"""
    
    def setUp(self):
        """
        Utworzenie ankiety i zestawu odpowiedzi do użycia 
        we wszystkich metodach testowych
        """
        question = "Jaki jest Twój ojczysty język?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['angielski', 'hiszpański', 'polski']

    def test_store_single_response(self):
        """
        Sprawdzenie czy pojedyncza odpowiedź jest prawidłowo
        przechowywana
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """
        Sprawdzenie czy trzy pojednyncze odpowiedzi są prawidłowo
        przechowywane
        """
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
