import math 
class MaxNumber:
    def __init__(self, num):
        self.num = num
    
    def getResult(self):
        return (math.pow(10, self.num)-1)