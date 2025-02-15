import random

# fruits = ["item1","item2"]
# print(fruits[0])
# print(fruits[1])
# fruits.append("item3")
# print(fruits)
# fruits.extend(["item4","item5"])
# print(fruits)
# print("Who's gonna pay the bill")
# friends = ["Alice","Bob","Charlie"]
# index = random.randint(0,2)
# print("Bill will be paid by",friends[index])
# print("Bill will be paid by",random.choice(friends))
# print(len(friends))
# print(friends[4])

ROCK='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''
PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''

SCISSOR = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  '''



choices =["ROCK","PAPER","SCISSOR"]



def display(choice):    
 if choice == "ROCK":
    print(ROCK)
 elif choice == "PAPER":
    print(PAPER)
 elif choice == "SCISSOR":
    print(SCISSOR)


def playGame():
   userChoice = input("Enter your choice ROCK PAPER or SCISSOR\n")

   if userChoice not in choices:
      print("Please select the correct choice")
      return
   computerChoice = random.choice(choices)
   print("Your Choice\n")
   display(userChoice)
   print("Computer Choice\n")
   display(computerChoice)
   if userChoice == computerChoice:
      print("Match draw")
   elif (userChoice == "ROCK" and computerChoice == "SCISSOR") or (userChoice == "PAPER" and computerChoice == "ROCK") or (userChoice == "SCISSOR" and computerChoice == "PAPER"):
      print("You Won")
   else:
      print("You Lose")
playGame()

