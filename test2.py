''''
second = 1
minute = 60 * second
hour = 60 * minute

m = 1
km = 1000 * m
ft = 0.3048 * m
mi = 1609.344 * m
kph = km / hour
mph = mi / hour

liter = 1
floz = 0.02957344 * liter

plane_altitude = 10_000 * ft
bottle = 20 * floz
speed_limit = 75 * mph

print(f'Plane altitude: {plane_altitude/m} m')
print(f'Bottle volume: { bottle/liter} l' )
print(f'Speed limit { speed_limit/kph:.1f} km/h')

# 10_000 -> 10tys.
# 10.000 -> 10
# :.1f -> zaokroglenie do jednego miejsca po przecinku
'''

'''
#DISTANE CONVERSION
m = 1337
km = m / 1000
mi = m / 1608
nm = m / 1852

print(f'Meters: {m}')                                           #int
print(f'Kilometers: {km}')                                      #float
print(f'Miles:  {mi:.2f}')                                      #float (two decimal places)
print(f'Nauticla Miles: {nm:.2f}')                              # ^
print(f'm: {m}, km: {int(km)}, mi: {mi:.1f}, nm: {nm:.1f}')     #int, int, float(1decimal), float(one decimal)
'''

# int, float, bool (T/F) , None / Not None, str

# bool
'''
a = bool(True) == True
b = bool(False) == False
c = (True) == True

print(a)
print(b)
print(c)
'''

# None / not None
'''
a = None is None
b = None is not None
c = bool(bool(None) is not bool(None)) == False
d = (bool(bool(None) is not bool(None)) == False and bool(None))
e = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None)

print(a)
print(b)
print(c)
print(d)
print(e)

f = not None is not None
print(f)
'''

# str
'''
my_str = """First Line
second line
third line"""
print(my_str)

print('\U0001F680')

name = input('What is your name: ')
print(f'Witaj {name}')
type(name)


age = input('What is your age? ')
print(f'My age is: {age}')
'''
'''
text = input('Write something here: ')
length = len(text)

print(f'Podany ciag ma: {length} znakow')


name = input('Write here your name: ')
#length = len(name)
print(f'Hello {name} \U0001F642 ')              # usmiechnieta buzia
'''


#name = input('Podaj swoje imie: ')

#text = (f"""'''My name is... "{name}".\n\tI\'m an \"\"\"astronaut!\"\"\"""")
#print(text)



'''
text = 'Andrzej'
print(f'\t{text}, \r{text}, \t {text},  \n\t{text}')
'''

'''
a = 'Python'
a = a.replace('P', 'J')
print(a)

a = 'Python'
b = a.replace('P', 'J')
print(a)
print(b)


a = '-' * 25
print(a)

name = input('wpisz imie: ')
name_upper = name.upper()
print(name_upper)
'''


print("Konwersja:")
a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")
print(float(a) + float(b))