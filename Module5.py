class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

validator = DataValidator()

validator.validate_email(email="bad-email")
validator.validate_age(age=200)

validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
my_dog2 = Dog(name="Max")

print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping
print(my_dog.bark())   # Buddy says woof!