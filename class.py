# Write a class that calculates and stores the height and weight
# of a person in metric. The file should be named lab.py.
# BMI is calculated using this formula:
# Weight/Height2
# - weight is in kilograms and height is in meters.
# • The class should have two properties named:
# 1. Weight
# 2. Height
# • The class should have one method that returns a float named
# (no arguments should be accepted):
# 1. BMI_Value
class BMI:
    def __init__(self,weight,height):
        self.weight=weight
        self.height=height

    def BMI_Value(self):
        return self.weight/(self.height**2)
x= BMI(70,1.75)
print(x.BMI_Value())