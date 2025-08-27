class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def move(self):
        print("The car is driving.")

class Bike(Vehicle):
    def move(self):
        print("The bike is pedaling.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing.")


# Polymorphism in action
vehicles = [Car(), Bike(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
