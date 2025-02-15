# print("Welcome to the Band Name Generator \n")
# city=input("What's the name of the city you grew up in \n")
# pet=input("What's your pet's name \n")
# print("Your band name could be"+" "+city+" "+pet)
#PEMDASLR
# print("Number of letters in your name: " + str(len(input("Enter your name"))) )
# height = int(input("What is your height"))
# if height >= 120:
#     print("can ride")
# else:
#     print("cannot ride")
# number =int(input("Enter the number"))
# if number%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")
# weight = float(input("Enter your weight"))
# height = float(input("Enter your height"))
# bmi = float(weight/(height**2))
# if bmi < 18.5:
#     print("Underweight")
# elif 18.5<=bmi <25:
#     print("normal weight")
# else:
#     print("Overweight")
print("Welcome to Python Pizza Deliveries")
size = str(input("What size of pizza do you want? S , M or L: "))
# want_pepperoni = str(input("Do you want pepperoni? Y or N"))
# want_extra_cheese = str(input("Do you want extra cheese? Y or N"))
if size == "S":
    bill = 15
    want_pepperoni = str(input("Do you want pepperoni? Y or N"))
    want_extra_cheese = str(input("Do you want extra cheese? Y or N"))

    if want_pepperoni=="Y":
     
     bill +=2
    if want_extra_cheese =="Y":
     bill +=1
    print(f"your bill is ${bill}")
elif size == "M":
    bill = 20
    want_pepperoni = str(input("Do you want pepperoni? Y or N"))
    want_extra_cheese = str(input("Do you want extra cheese? Y or N"))

    if want_pepperoni=="Y":
     
     bill +=3
    if want_extra_cheese =="Y":
     bill +=1
    print(f"your bill is ${bill}")
elif size== "L":
    bill =25
    want_pepperoni = str(input("Do you want pepperoni? Y or N"))
    want_extra_cheese = str(input("Do you want extra cheese? Y or N"))

    if want_pepperoni=="Y":
     
     bill +=3
    if want_extra_cheese =="Y":
     bill +=1
    print(f"your bill is ${bill}")
else:
   print("This size is not available")






 
