#  Planet Weights

weight = float(input("Enter your weight on planet earth: "))
planet_number = int(input("Enter the number of the planet you want to fight on: "))

if planet_number == 0:
    weight = weight * 0.38
elif planet_number == 1:
    weight = weight * 0.91
elif planet_number == 2:
    weight = weight
elif planet_number == 3:
    weight = weight * 0.38
elif planet_number == 4:
    weight = weight * 2.53
elif planet_number == 5:
    weight = weight * 1.07
elif planet_number == 6:
    weight = weight * 0.89
elif planet_number == 7:
    weight = weight * 1.14
else:
    print("Invalid planet number")

print("Your weight on planet", planet_number, "is", weight)
    