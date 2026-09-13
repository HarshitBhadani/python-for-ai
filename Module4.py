try:
    result = 10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print(f"{self.name} says Meow!")

jack = Dog("Jack", "Labrador")
jack.bark()

tom = Cat("Tom", "Siamese")
tom.meow()