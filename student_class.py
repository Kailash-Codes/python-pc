class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
         print(self.name,self.roll)

anupam = Student("anupam",14)

print(anupam.display())