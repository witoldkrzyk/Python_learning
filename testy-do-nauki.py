class Iris:
    pass

flower = Iris()
flower.sepal_length = 5.1
flower.sepal_width = 3.5
flower.petal_lenght = 1.4
flower.petal_width = 0.2
flower.species = 'setosa'

print(flower.__dict__)
