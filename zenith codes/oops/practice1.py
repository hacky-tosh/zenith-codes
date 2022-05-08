class Programmer:
    company = 'Google'

    def __init__(self, name, product):
        self.name = name 
        self.product = product
    
    def getInfo(self):
        print(f'The name of the programmer is {self.name} and the product is {self.product} Thank You!')

emp1 = Programmer("Ashu","Online Portal")
emp2 = Programmer("Yash", "Portfolio Site")
emp1.getInfo()
emp2.getInfo()

