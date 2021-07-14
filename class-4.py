class Employe:
    salary = 'One Crore'

    def instanceMethod(self): #Instance Method
        print(self.__dict__)
CodeWithSingh = Employe() # Object of the class employe
CodeWithSingh.name = "Start"
CodeWithSingh.salary = "one crore"
CodeWithSingh.instanceMethod()