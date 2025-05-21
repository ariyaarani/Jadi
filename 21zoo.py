# Author: Mohammad Reza Arani

class Animal:
    zoo_name = "Central Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Zoo: {Animal.zoo_name}")

    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age}, Sound: {self.sound}"


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"Bird sound: {self.sound}")

    def info(self):
        super().info()
        print(f"Wing Span: {self.wing_span} meters")


if __name__ == "__main__":
    lion = Animal("Lion", "Panthera leo", 5, "Roar")
    print(lion)
    lion.make_sound()
    lion.info()


    parrot = Bird("Parrot", "Psittaciformes", 2, "Squawk", 0.4)
    print(parrot)
    parrot.make_sound()
    parrot.info()
