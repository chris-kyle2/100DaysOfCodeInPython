class Person:
    gender = "male"
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def bmi(self):
        return self.weight / self.height ** 2

person1 = Person("John",20,1.75,70)
person2 = Person("Jane",21,1.65,55)

print(person1.bmi())
print(person2.bmi())


# Create a class called Car that has the following attributes: make, model, year, and color.
# The class should have the following methods: drive, stop, and get_info.