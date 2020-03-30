
#   __dict__)   #
'''
class Iris:
    pass

flower = Iris()
flower.sepal_length = 5.1
flower.sepal_width = 3.5
flower.petal_lenght = 1.4
flower.petal_width = 0.2
flower.species = 'setosa'

print(flower.__dict__)
'''



# __init__  #
#walidacja na float i int

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