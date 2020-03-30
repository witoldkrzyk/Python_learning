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


def power(x, y=None):   #2 warunek opcjonalny
    if y is None: 
        x = y
       
        return x**y

print(power(4, 3))
print(power(3))

 