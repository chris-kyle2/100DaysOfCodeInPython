class BMI:
    def __init__(self,weight,height):
        self.weight=weight
        self.height= height
    def claculateBMI(self):
        return self.weight/(self.height**2)
    
    
    
x= BMI(75,1.72)
print(x.claculateBMI())