# Będziemy przeprowadzać testy jednostkowe w Pythonie

# 11.1
#import city_functions as cc


#print(cc.city_country('warszawa', 'polska', 37000000))
#print(cc.city_country('warszawa', 'polska'))
#print(cc.city_country('moskwa', 'federcja rosyjska', 127000000))

#from Survey import AnonymousSurvey

##Zadeklarowanie pytania i utworzenie odpowiedzi
#question = "Jaki jest Twój ojczysty język?"
#my_survey = AnonymousSurvey(question)

##Wyświetleni pytania i przechowanie odpowiedzi na nie
#my_survey.show_question()
#print("Wpisz 'q' aby zakończyć działanie programu.\n")
#while True:
#    response = input("Język: ")
#    if response == 'q':
#        break
#    my_survey.store_response(response)

##Wyświetlenie wyników ankiety
#print("\nDziękujemy za udział w ankiecie")
#my_survey.show_results()

#11.3

class Employee():
    """Podstawowe informacje o pracowniku"""
    
    def __init__(self, imie, nazwisko, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie = wynagrodzenie

    def give_raise(self, value=''):
        """Zwiększa wynagprdzenie pracownika (domyślnie o 5000 zł) """
        if value:
            self.wynagrodzenie += value
        else:
            self.wynagrodzenie += 5000



