class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

class Student2(Student):
    pass

sachit = Student2("sachit",12)
print(sachit.display())