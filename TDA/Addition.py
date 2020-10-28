class Addition:
    def __init__(self, num):
        self.num1 = num % 10
        self.num2 = (num - self.num1)/10
    
    def getResult(self):
        return self.num1 + self.num2