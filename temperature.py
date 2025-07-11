from array import array

days = int(input("How many days temperature? "))
temperature = []

def temperature_list(temperature):
    for i in range(days):
        t = int(input(f"Day {i+1} temperature: "))
        temperature.append(t)
    
    return temperature

temperature_list(temperature)
print(temperature)

def average_temperature(temperature):
    sum=0
    for i in temperature:
        sum += i
    avg_temp = sum/len(temperature)
    
    return avg_temp
print(f"The average temperature is {average_temperature(temperature)}")

def above_average_temperature(temperature,avg_temp):
    count = 0
    for j in temperature:
        if j > avg_temp:
            count +=1
    return count
print(f"The number of days above average temperature is {above_average_temperature(temperature,average_temperature(temperature))}")