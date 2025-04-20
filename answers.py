class Superhero:
    def __init__(self, name, alias, power, strength_level):
        self.name = name
        self.alias = alias
        self.power = power
        self.strength_level = strength_level  # 1 to 100
        self.health = 100

    def introduce(self):
        return f"I am {self.alias}, known as {self.name}. My power is {self.power}!"

    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(0, self.health)
        return f"{self.alias} took {damage} damage. Health is now {self.health}."

    def is_alive(self):
        return self.health > 0

        class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying through the sky!")


class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling down the path!")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing across the water!")

    # Question 2

    class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying through the sky!")


class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling down the path!")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing across the water!")

# END OF ASSIGNMENT


