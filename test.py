import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def view_cars(self):
        return f"{self.make} - {self.model} ({self.color})"

os.system("cls")

cars = []

while True:
    make = input("Enter car make (or type 'stop' to finish): ")
    if make.lower() == 'stop':
        break
    
    model = input("Enter car model: ")
    color = input("Enter car color: ")
    
    cars.append(Car(make, model, color))
    print("Car added!\n")

print("\nList of all cars:")
for car in cars:
    print(car.view_cars())