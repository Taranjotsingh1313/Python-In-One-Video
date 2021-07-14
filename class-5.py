class Employe:
    salary = 'One Crore'

    def instanceMethod(self): #Instance Method
        print(self.__dict__)
    # Class Methods
    @classmethod
    def classMethod(cls):
        cls.salary = 10
CodeWithSingh = Employe() # Object of the class employe
CodeWithSingh.name = "Start"
print(CodeWithSingh.salary)
Employe.classMethod()
print(CodeWithSingh.salary)