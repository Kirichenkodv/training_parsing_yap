# Импортируйте модуль для работы с регулярными выражениями.
import re


addresses = [
    (
        "Он проживал в городе Иваново на улице Наумова. "
        "Номер дома 125 был зеркальной копией его номера квартиры 521"
    ),
    "Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.",
]

city_pattern = r"город[а-я]?\ [а-яА-Я]+"
street_pattern = r"улиц[а-я]?\ [а-яА-Я]+"
house_number_pattern = r"дом[а-я]?\ [\d]*"
apartment_number_pattern = r"квартир[а-я]?\ [\d]*"


for address in addresses:
    city = re.search(city_pattern, address).group().split()[-1]
    street = re.search(street_pattern, address).group().split()[-1]
    house_number = re.search(house_number_pattern, address).group().split()[-1]
    apartment_number = re.search(apartment_number_pattern, address).group().split()[-1]

    print(f"{city} {street} {house_number} {apartment_number}")


