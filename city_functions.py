def city_country(city, country, population=''):
    """ Zwraca ciąg 'City, Country' z argumentów wywołania"""
    if population:
        message = str(city).title() + ", " + str(country).title() + ", populacja: " + str(population)
    else:
        message = str(city).title() + ", " + str(country).title() 
    return message

