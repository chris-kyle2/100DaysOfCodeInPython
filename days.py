# Write a program that reads in a number and prints the date that
# number of days from now in this format:
# Saturday, February 6, 2021
import datetime
days_from_now = int(input("Enter the number of days from now: "))
required_date = datetime.datetime.now() + datetime.timedelta(days=days_from_now)
print(required_date.strftime("%A, %B %d, %Y"))




