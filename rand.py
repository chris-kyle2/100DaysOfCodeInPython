###Write a program that reads a number and prints it Small, Medium or Large
# depending on if the number is below 100 or above 200.
# • For example, if the user enters 150 the program should
# display “Medium”
# • Or, if the user enters 50 the program should display “Small”
input_number = int(input("Enter a number please\n"))
def check_number(input_number):
    if (input_number < 100):
        print("Small")
    elif(input_number >100 and input_number<200):
        print("Medium")
    else:
        print("Large")

check_number(input_number)