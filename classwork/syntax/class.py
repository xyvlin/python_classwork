class Person: 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hi, I'm {self.name} and {self.age} years old.")
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name,age)
        self.school=school
    def introduce(self):
        print(f"Hello, I'm {self.name}. I'm {self.age} years old and from {self.school}.")

p = Person("person",5)
p.introduce()
s = Student("name",14,"human school")
s.introduce()