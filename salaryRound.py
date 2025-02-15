### salary round off to the zero decimal places per month

input_salary = float(input("Enter your yearly salary: "))
def salary_round(input_salary):
    monthly_salary = input_salary / 12
    rounded_salary = round(monthly_salary,3)
    return rounded_salary


print(salary_round(input_salary))