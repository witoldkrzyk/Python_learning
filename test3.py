############LISTY
'''
my_list = [1, 2, 3, 4, 5]

print(my_list)

#
a = 'come'
print(a)

#
my_list = [1,2]
a = my_list + [3,4]

print(a)

#
my_list = ['a', 'b', 'c', 'd']

print(my_list)
del my_list[3]

print(my_list)

#
my_list = [1,3,6,7,8,6]

a = sorted(my_list)
print(my_list)
print(a)

#
my_list = [1,3,6,7,8, 10]

my_list.sort()

my_list.append(1)
print(my_list)

#

a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']

print(a)
print(b)
print(c)

#

a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']

a[0] = b[4]
b[4] = a[4]
del c[4]


print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
'''
'''
##############TUPLE


a = '-' * 20
print (a)


my_set = {1, 2, 3}

value = my_set.pop()

print(my_set)
print(value)
'''

'''
DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]

a = DATA[2]
print(a)

b = DATA[2][2]
print(b)

c = len(DATA)
print(c)

d = len(DATA[2])
print(d)


LIST = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

e = LIST[0][0]
f = len(LIST)
g = LIST[2][2]


print(e)
print(f)
print(g)


job = 'astronauts'

if job == 'astronaut':
    print('Astronauts are from USA')
else: 
    print('Nie jestes astronautom!')

a = 2**3 
print(a)

'''
'''
#sprawdzanie czy liczba jest parzysta!
value = int(input('Podaj liczbę: '))
#value = int(value)

if value % 2 != 0:
    print('Liczba nie jest parzysta!')
else:
    print('Liczba  jest parzysta!')
    

language = 'Polski'
'''
'''
#czy jest pelnoletni?
age = int(input('Podaj wiek: '))

if age >= 18:
    print(f' Wiek uzytkownika to: {age} lat. Użytkownik jest pelnoletni! ')
else: 
    print('Użytkownik nie jest pełnoletni!')
'''

question = input('Jaka marke samochodu posiadasz?')

if question == 'skoda':
    print("Super!")
elif question == 'seat':
    print("Elegancko")
elif question == 'volvo':
    print("Bardzo bezpiecznie!")
