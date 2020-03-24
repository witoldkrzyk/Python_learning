#calculator

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('To nie jest liczba! Wpisz liczbę')
            continue
        else:
            return userInput
            break


print("Witaj w kalkulatorze ! \U0001F642")

dash = '-' * 30
print(dash)

#dodawanie
def addition(x, y):
    return x + y

#odejmowanie 
def subtraction(x, y):
    return x - y

#mnozenie 
def multiplication(x, y):
    return x * y

#dzielenie 
def division(x, y):
    return x / y 

#potegowanie 
def exponentiation(x, y):
    return x ** y

#modulo
def modulo(x, y):
    return x % y

#dzielenie_zaokraglone  
def trueDivision(x, y):
    return x // y

print('Wybierz operacje: ')
print('1. Dodawanie')
print('2. Odejmowanie')
print('3. Mnozenie')
print('4. Dzielenie')
print('5. Potegowanie')
print('6 Modulo pierwszej z drugiej')
print('7. Dzielenie zaokrąglone')
choice = inputNumber('Wybierz co chcesz zrobic: 1 / 2 / 3 / 4 / 5 / 6 / 7 :  ')

x = inputNumber('Wpisz pierwszą liczbę: ')
y = inputNumber('Wpisz drugą liczbę: ')



if choice == 1: 
    print(f'{x} + {y} = {addition(x, y)}')

elif choice == 2:
    print(f'{x} - {y} = {subtraction(x, y)}')

elif choice == 3:
    print(f'{x} * {y} = {multiplication(x, y)}')

elif choice == 4:
    print(f'{x} / {y} = {division(x, y)}')

elif choice == 5:
    print(f'{x} ^ {y} = {exponentiation(x, y)}')

elif choice == 6:
    print(f'{x} % {y} = {modulo(x, y)}')

elif choice == 7:
    print(f'({x} // {y} = {trueDivision(x, y)}')