import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int (input("How many numbers do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))

password_list = []

for item in range(0,nr_letters):
    password_list.append(random.choice(letters))
print(password_list)

for item in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)

for item in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
password = ""

for item in password_list:
    password += item
print(f"Your password is: {password}")