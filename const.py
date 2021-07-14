class Employe:
    salary = 'One Crore'

    def __init__(self,name):
        self.name = name
        print("This is constructor and runs when object of class is intialized")


cws = Employe('Cws')
print(cws.name)

