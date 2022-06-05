# write a class Train which has methods to book a ticket , get status (no of seats) and get fare information of trains running udner Indian Railways

class Train():
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats are available in the train are{self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is :{self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("sorry this train is full! kindly try in tatkal")        
intercity = Train("Intercity express: 132649",92,2)
intercity.getStatus()
intercity.bookTicket() #has 2 tickets
intercity.getStatus()
intercity.bookTicket() # has 1 ticket left
intercity.bookTicket() # no ticket left
intercity.fareInfo()