'''
filename = input('Type filename: ')

try:
    with open(filename) as file:
        print(file.read())

except FileNotFoundError:
    print('Sorry, the file not found')

except PermissionError:
    print('sorry, you are not permitted')
'''



'''
def divide(a, b):
    if b != 0:
        return a / b 


print(divide(4, 2))
print(divide(4, 0))
'''

'''
def power(x, y=None):   #2 warunek opcjonalny
    if y is None: 
        x = y
       
        return x**y

print(power(4, 3))
print(power(3))
'''

'''
# Nazwa klasy ma CamelCase a nie snake_case 

class Astronaut:
    pass

class Cosmonaut:
    pass

mark = Astronaut()
melissa = Astronaut()
ivan = Cosmonaut()
jan = Cosmonaut()
 



 # jedna klasa jedna instancja = OBIEKT przyklad nizej ale moga byc na jedna klase wiele instancji

class Iris:
    pass

flower = Iris()




# zadanie 1

class Iris:
    pass

setosa = Iris()
virginica = Iris()
versicolor = Iris()


#zadanie 2 

class Astronaut:
    pass

class SpaceAgency:
    pass

twardowski = Astronaut()
watney = Astronaut()

nasa = SpaceAgency()
esa = SpaceAgency()
polsa = SpaceAgency()   

# instancja = obiekt w klasie
# atrybuty inaczej definiowane jako WLASCIWOSCI LUB POLA
# atrybuty przechowuja informacje (stan ktory moze sie zmieniac wraz z zyciem obiektu - reprezentuje biezacy stan obiektu) dla obiektów

# dynamiczne atrybuty

#zad1

class Temperature:
    pass

temp = Temperature()
temp.kelvin = 10 

print(temp.kelvin)

#zad2

class Astronaut:
    pass

astro = Astronaut()

astro.first_name = 'Jose'           #snake_case -> atrybut
astro.second_name = 'Jimenez'

print(f'My name...{astro.first_name}{astro.second_name}')


#zad3

class Iris:
    pass

setosa = Iris()

setosa.features = [5.1, 3.5, 1.4, 0.2]
setosa.label = 'setosa'

print(setosa.label)
sum(setosa.features)



#dostep do nieistniejacych atrybutow 
#AttributeError : nie ma takiego atrybutu jak 'missions'
class Astronaut:
    pass

astro = Astronaut()

print(astro.missions)


#uzyskiwanie wszystkich atrybutow / wartosci   ->       .__dict__  

class Iris:
    pass

flower = Iris()
flower.sepal_length = 5.1
flower.sepal_width = 3.5
flower.petal_lenght = 1.4
flower.petal_width = 0.2
flower.species = 'setosa'

print(flower.__dict__)


#   zadanie1 z konca   #

#INPUT

'''
#Jan, Twardowski, 1961-04-12
#Mark, Watney, 1969-07-21
#ESA, European Space Agency, Europe
#NASA, National Aeronautics and Space Administration, USA
#POLSA, Polish Space Agency, Poland
'''


class Astronaut():
    pass

class SpaceAgency():
    pass

twardowski = Astronaut()
twardowski.first_name = 'Jan'
twardowski.last_name = 'Twardowski'
twardowski.date_birth = '1961-07-21'

watney = Astronaut()
watney.first_name = 'Mark'
watney.last_name = 'Watney'
watney.date_birth = '1969-07-21'

esa = SpaceAgency()
esa.short_name = 'ESA'
esa.long_name = 'European Space Agency'
esa.location = 'Europe'

nasa = SpaceAgency()
...

polsa = SpaceAgency()
...

# INIZJALIZACJA 

#metoda inicjalizacji bez argumentow 

#zad1

class Astronaut:
    def __init__(self):
        print('My name... Andrzej Lewy')

andrzej = Astronaut()

# z argumentami 

#zad2

class Astronaut():
    def __init__(self, name):
        print('My name... {name}')

jose = Astronaut('Jose Jimenez')
#my name... Jose Jimenez

mark = Astronaut(name = 'Mark Watney')
#my name... Mark Watney

ivan = Astronaut()
#typeError: brakuje 'name'


#zad3
#atrybuty czasu poczatkowego

class Astronaut():
    def __init__(self):
        self.first_name = 'Mark'
        self.last_name = 'Watney'


mark = Astronaut()
print(mark.first_name)      #mark
print(mark.last_name)       #watney
print(mark.missions)        #error

ivan = Astronaut()
print(ivan.first_name)      #mark
print(ivan.last_name)       #watney
print(watney.missions)      #error

#zad4

class Astronaut:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

mark = Astronaut('Mark', 'Watney')

print(mark.first_name)      #Mark
print(mark.last_name)       #watney

ivan = Astronaut(first_name = 'Ivan', last_name = 'Ivanovich')

print(ivan.first_name)          #ivan
print(ivan.last_name)           #ivanovich


#zad4

class Astro:
    def __init__(self, first_name, last_name):
        self.full_name = f'{first_name}{last_name}'

mark = Astro('Mark', 'Watney')

print(mark.full_name)       # mark watney
print(mark.first_name)      # mark
print(mark.last_name)       #watney


'''
#sprawdzanie wartosci
#zad5

class Kelvin:
    def __init__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('Temperature must be int or float')

        if value < 0.0:
            raise ValueError('Temperature must be greater than 0')

        self.value = value
    
ice = Kelvin(273.15)
print(ice.value)
#273.15

not_existing = Kelvin(-300)
#ValueError



#dokonczyc zadania z 10.3.5 