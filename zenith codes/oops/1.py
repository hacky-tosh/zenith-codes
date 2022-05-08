class RailwayForm:
    formtype = 'Railway form'

    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')

ashu = RailwayForm()
ashu.name = 'Ashutosh'
ashu.train = 'Manali'
ashu.printData() 


class Emp:
    company = 'Google'
    sallery = 500

ashu = Emp()
yash = Emp()
print(ashu.company)
print(yash.company)
Emp.company = "Alphabet"
print(ashu.company)
print(yash.company)
ashu.sallery = 100
# yash.sallery = 200
print(ashu.sallery)
print(yash.sallery)