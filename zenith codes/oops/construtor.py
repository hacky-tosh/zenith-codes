class Emp:
    company = 'Google'

    def __init__(self,name, salary, age):
        self.name = name 
        self.salary = salary
        self.age = age 
        print("Init runs")

    def getDetails(self):
        print(f'The name of the employee is {self.name} salary is {self.salary} and age is {self.age}')

    def getSalary(self):
        print('Sallery is 1000k')


ashu = Emp("ashu",10000,20)
yash = Emp("yash",200000,20)
ashu.getDetails()
yash.getDetails()
