class Employe:
    salary = 'One Crore'

    def instanceMethod(self): #Instance Method
        print(self.__dict__)
    # Class Methods
    @classmethod
    def classMethod(cls):
        cls.salary = 10
    
    @staticmethod
    def staticMethod(a):
        print("This is simple static " + a)
CodeWithSingh = Employe() # Object of the class employe

Employe.staticMethod("' Run By Employee  Class ' ")
CodeWithSingh.staticMethod("' Run By CodeWithSingh Object  Class '")