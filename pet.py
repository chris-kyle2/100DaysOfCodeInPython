class Pet:
    def __init__(self,name,species,age,price):
        self.name=name
        self.species=species
        self.age=age
        self.price=price
   
    def birthday(self):
        self.age +=1
        return self.age
    def apply_discount(self ,discount):
        self.price *= (1-discount)
        return self.price
    
    def get_info(self):
        return f"Name: {self.name}, Species: {self.species},Age: {self.age} ,Price: {self.price}"
    
pet1 =Pet("Buddy","Dog",3,100)
print(pet1.birthday())
print(pet1.apply_discount(0.1))
print(pet1.get_info())
print(pet1.name)
print(pet1.species)
print(pet1.age)
print(pet1.price)

pet2 =Pet("Whiskers","Cat",2,50)
print(pet2.birthday())
print(pet2.apply_discount(0.2))
print(pet2.get_info())

