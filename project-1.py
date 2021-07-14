import random
inputofuser = int(input("Enter Number Between 1 to 10: \n"))
randomnumber = random.randint(1,10)
if inputofuser == randomnumber:
    print("User Wins And The Number Was" ,randomnumber)
else:
    print("Computer Wins And The Number Was " ,randomnumber)