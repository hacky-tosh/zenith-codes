class Pnr:

    def __init__(self,name,fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f'The name of the Train is {self.name}')
        print(f'The seats availble in the train are {self.seats}')

    def fareInfo(self):
        print(f'The price of the ticket is : Rs{self.fare}')

    def bookTicket(self):
        if(self.seats>0):
            print(f'Your ticket has been booked! Your seat number is {self.seats}')
            self.seats -= 1
        else:
            print("Sorry This train is full!")

    # def cancelTicket(self):



train1 = Pnr("rajdhani", 500, 10)
train1.getStatus()
train1.fareInfo()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.getStatus()
