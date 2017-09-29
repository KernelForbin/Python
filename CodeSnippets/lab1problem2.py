__author__ = 'Kenny Mitchell'
# Problem 2
word1 = input("Please input your first word: ")
word2 = input("Please input your second word: ")
if word1 == word2:
    print("These words are the same.")
else: print("These words are not the same.")

#To Problem 3 *messing around/experimenting, not to be part of assignment*
while 1:
    proceed = input("\nContinue to Lab 1 Problem 3? y or n: ")
    if proceed == "y":
        import lab1problem3
    elif proceed == "n":
        print("\nVery well. Run me again any time!\n")
        input('Press the Enter Key To Exit...\n\n\n')
        exit()
    else:
        print("Not a valid selection.")