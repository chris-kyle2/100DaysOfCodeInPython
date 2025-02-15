### rounding off a number to the given number of decimal places
number = 12.3456789
rounded_number = round(number,2)
print(rounded_number)

def round_number(number,decimal_places):
    print(f"Rounding {number} to {decimal_places} decimal places")
    rounded_number = round(number,decimal_places)
    print(f"The rounded number is {rounded_number}")

round_number(12.3456789,2)
round_number(12.3456789,3)
round_number(12.3456789,4)
round_number(12.3456789,5)
round_number(12.3456789,6)
round_number(12.3456789,7)
round_number(12.3456789,8)