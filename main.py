from datetime import date
# This is Test

# THis is jaydip
class Person:
    
    def __init__(self, name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year - year)


p1 = Person('jaydip',21)
p2 = Person.fromBirthYear('kishan',2000)

print(p1.age)
print(p2.age)
        
    