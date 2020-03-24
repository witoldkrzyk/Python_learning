#calculator dwoch liczb

print("Witaj w kalkulatorze ! \U0001F642")

myslniki = '-' * 30
print(myslniki)

#dodawanie
def dodawanie(x, y):
    return x + y

#odejmowanie 
def odejmowanie(x, y):
    return x - y

#mnozenie 
def mnozenie(x, y):
    return x * y

#dzielenie 
def dzielenie(x, y):
    return x / y 

#potegowanie 
def potegowanie(x, y):
    return x ** y

#modulo
def modulo(x, y):
    return x % y

print('Wybierz operacje: ')
print('1. Dodawanie')
print('2. Odejmowanie')
print('3. Mnozenie')
print('4. Dzielenie')
print('5. Potegowanie')
print('6 Modulo pierwszej z drugiej')

wybor = int(input('Wybierz co chcesz zrobic: 1 / 2 / 3 / 4 / 5 / 6 :  '))

x = float(input('Wpisz pierwsza liczbe: '))
y = float(input('Wpisz druga liczbe: '))



if wybor == 1: 
    print(f'{x} + {y} = {dodawanie(x, y)}')

elif wybor == 2:
    print(f'{x} - {y} = {odejmowanie(x, y)}')

elif wybor == 3:
    print(f'{x} * {y} = {mnozenie(x, y)}')

elif wybor == 4:
    print(f'{x} / {y} = {dzielenie(x, y)}')

elif wybor == 5:
    print(f'{x} ^ {y} = {potegowanie(x, y)}')

elif wybor == 6:
    print(f'{x} % {y} = {modulo(x, y)}')