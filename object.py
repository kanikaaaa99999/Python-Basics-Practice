
"""object is a bundle of related attributes (variables) and methods (functions)
that together encapsulate a set of related functionalities for object manipulation"""

#class =( "blueprint for creating objects, defining their attributes and behaviors")

from car import car

car1 = car("toyota", 2020, "red", True)
car2 = car("honda", 2019, "blue", False)
car3 = car("ford", 2021, "black", True)

# Using the car objects
print("Car 1:")
print(f"Model: {car1.model}, Year: {car1.year}, Colour: {car1.colour}")
car1.drive()
car1.stop()

print("\nCar 2:")
print(f"Model: {car2.model}, Year: {car2.year}, Colour: {car2.colour}")
car2.honk()
car2.sell()

print("\nCar 3:")
print(f"Model: {car3.model}, Year: {car3.year}, Colour: {car3.colour}")
car3.park()
car3.sell()



