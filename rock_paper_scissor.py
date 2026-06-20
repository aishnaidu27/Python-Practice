import random

choice=['Rock','Paper','Scissors']


user=input("Enter rock,paper or scissor").capitalize()

computer_choose=random.choice(choice)

print("user choosed",user)
print("computer_choosed",computer_choose)

if user==computer_choose:
    print("Draw!!")
elif user=="Rock" and computer_choose=="Scissors":
    print("You won")
elif user=="Paper" and computer_choose=="Rock":
    print("You won")
elif user=="Scissors" and computer_choose=="Paper":
    print("You won")
else:
    print("computer won")


