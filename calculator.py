print("======Calculator======")

num1=float(input("Enter the value of number 1:"))
num2=float(input("Enter the value of number 2:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulas")
print("6.Power")

operation=input("Enter the operation You want to apply(1-6):")

if operation=="1":
    print("Your choice is addition (+):",num1+num2)

elif operation=="2":
    print("Your choice is subtraction (-):",num1-num2)

elif operation=="3":
    print("Your choice is Multiplication (*):",num1*num2)

elif operation=="4":
    if num2!=0:
        print("Your choice is Division (/):",num1/num2)
    else:
        print("number divided by zero not possible")

elif operation=="5":
    print("Your choice is Modulas (%):",num1%num2)

elif operation=="6":
    print("Your choice is Power (*):",num1**num2)

else:
    print("invalid operation")

