# Learn Pyhton The Hard Way ex39 - Dictionaries Study Drills
# Manuel Lameira
kantons = {
    'Zürich': 'ZH',
    'Bern': 'BE',
    'Luzern': 'LU',
    'Uri': 'UR',
    'Schwyz': 'SZ',
    'Obwalden': 'OW',
    'Nidwalden': 'NW',
    'Glarus': 'GL',
    'Zug': 'ZG',
    'Freiburg': 'FR',
    'Solothurn': 'SO',
    'Basel-Stadt': 'BS',
    'Basel-Landschaft': 'BL',
    'Schaffhausen': 'SH',
    'Appenzell Ausserrhoden': 'AR',
    'Appenzell Innerrhoden': 'AI',
    'St. Gallen': 'SG',
    'Graubünden': 'GR',
    'Aargau': 'AG',
    'Thurgau': 'TG',
    'Tessin': 'TI',
    'Waadt': 'VD',
    'Wallis': 'VS',
    'Neuenburg': 'NE',
    'Genf': 'GE',
    'Jura': 'JU'
}

cities = {
    'ZH': 'Winterthur',
    'BE': 'Thun',
    'LU': 'Emmen',
    'UR': 'Altdorf',
    'SZ': 'Einsiedeln',
    'OW': 'Sarnen',
    'NW': 'Stans',
    'GL': 'Glarus Nord',
    'ZG': 'Baar',
    'FR': 'Bulle',
    'SO': 'Grenchen',
    'BS': 'Riehen',
    'BL': 'Allschwil',
    'SH': 'Schaffhausen',
    'AR': 'Herisau',
    'AI': 'Appenzell',
    'SG': 'Rorschach',
    'GR': 'Chur',
    'AG': 'Baden',
    'TG': 'Frauenfeld',
    'TI': 'Lugano',
    'VD': 'Montreux',
    'VS': 'Sitten',
    'NE': 'Le Locle',
    'GE': 'Lancy',
    'JU': 'Delsberg'
}
# print out some cities
print('-' * 10)
print("Uri is the abbreviation: ", kantons['Uri'])
print("ZH has the city: ", cities['ZH'])
# print(f"TI is the abbreviation: {kantons['TI']}") # you can't call the second argument


# print every kantons abbreviation
print('-' * 10)
for kantons, abbrev in list(kantons.items()):
    print(f"{kantons} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# print every city in kantons
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
