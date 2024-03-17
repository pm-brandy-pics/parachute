class TicketBooking:
    def __init__(self,number,name,fare):
        self.tkno=number
        self.name=name 
        self.fare=fare 
    def show(self):
        print('Ticket number',self.tkno,'Name:',self.name,'Fare',self.fare)
list=[]
list.append(TicketBooking(1,'Arigato',6000))
list.append(TicketBooking(2,'Elgato',7000))
print('Result')
for i in range(2):
    print('Ticket number:',list[i].tkno)
    print('Name:',list[i].name)
    print('Fare:',list[i].fare)