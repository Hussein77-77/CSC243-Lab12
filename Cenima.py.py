class Hall:
    def __init__(self,name,seats):
        self.name=name
        self.__seats=seats
    def get_seats(self):
        return self.__seats
    def __has_seats(self):
        if self.__seats>0:
            return True
        elif self.__seats==0:
            return False
    def has_seats(self):
        return self.__has_seats()
    def set_seats(self,n):
        if 0<=n<=100:
            self.__seats=n
        else:
            print("Invalid seats.")
    def __str__(self):
        return f"Hall {self.name}: {self.__seats} seats"
class Guest:
    def __init__(self,name,tickets):
        self.name=name
        self.__tickets=tickets
    def get_tickets(self):
        return self.__tickets
    def add_tickets(self,n):
        if n>0:
            self.__tickets+=n
        else:
            print("Invalid amount.")
    def __str__(self):
        return f"{self.name}: {self.__tickets} tickets"
def reserve(Hall,Guest,n):
    if Hall.has_seats():
        Guest.add_tickets(n)
    else:
        print("Hall is full.")
        
    
                                                                                                                     
