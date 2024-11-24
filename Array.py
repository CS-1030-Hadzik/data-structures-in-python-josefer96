class vehicle:
    all_cars = {}
    def __init__(self, make, model, year):
            self = self
            self.make = make
            self.model = model
            self.year = year
cars = ['Ford','chrysler','dodge','Ram','jeep','chevy','GMC']

print(cars)
x = len(cars)
print (x)

cars.append('buick')

print(cars)

cars.insert(3,'toytoa')

print(cars)

cars.pop(5)

print(cars)

array = cars.__len__
print (array, 4)

cars.sort()
print(cars)

cars.sort(reverse= True)
print(cars)

