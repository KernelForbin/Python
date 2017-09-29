__author__ = 'Kenny Mitchell'
# Problem 3
x = input("Please input a value: ")
y = input("Please input anohter value: ")
print("x has the value: " + x)
print("y has the value: " + y)
z = x
x = y
y = z
print("x has the value: " + x)
print("y has the value: " + y)

#To Problem 4 *messing around/experimenting, not to be part of assignment*
while 1:
    proceed = input("\nContinue to Lab 1 Problem 4? y or n: ")
    if proceed == "y":
        import lab1problem4
    elif proceed == "n":
        print("\nVery well. Run me again any time!\n")
        input('Press the Enter Key To Exit...\n\n\n')
        exit()
    else:
        print("Not a valid selection.")