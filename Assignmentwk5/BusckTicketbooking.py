class Bus:

    def __init__(self,route,total_seats):
        self.route=route
        self.total_seats=total_seats
        self.booked=[]

    def book_seat(self,seat_number,passenger_name):

        for booking in self.booked:
            if booking[0]==seat_number:
                print("Seat already booked")
                return

        self.booked.append((seat_number,passenger_name))

    def available_seats(self):
        return self.total_seats-len(self.booked)

    def passenger_list(self):
        print("Passenger List")

        for booking in self.booked:
            print("Seat",booking[0],"-",booking[1])


bus=Bus("Kathmandu - Pokhara",10)

bookings=[
(3,"Ramila Shrestha"),
(7,"Deepak Gurung"),
(3,"Anita Rai"),
(1,"Prakash Magar"),
(7,"Suman Tamang")
]

for seat,name in bookings:
    bus.book_seat(seat,name)

print("Available Seats:",bus.available_seats())
print()

bus.passenger_list()