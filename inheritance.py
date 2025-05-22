# Write a class that calculates and stores the height and weight
# of a person in metric. The file should be named lab.py.
# BMI is calculated using this formula:
# Weight/Height2
# - weight is in kilograms and height is in meters.
# • The class should have two properties named:
# 1. Weight
# 2. Height
# • The class should have two methods:
# 1. BMI_Value – This takes no arguments and returns a decimal value of the BMI
# 2. Equals – This should Overload the equals method from the Object class to
# compare the weight and height of two BMI objects. 
class BMI:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    def Equals(self,other):
        return self.BMI_Value() == other.BMI_Value()

class BMI_Metric(BMI):
    def __init__(self,height,weight):
        super().__init__(height,weight)
        