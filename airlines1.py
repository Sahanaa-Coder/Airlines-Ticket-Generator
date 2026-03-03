class Airlines:
    def __init__(self, name_airlines, name_passenger, journey_date,
                 flight_time, starting_point, ending_point,
                 booking_id, travel_ticket, food_bill, snacks_bill):
        
        self.name_airlines = name_airlines
        self.name_passenger = name_passenger
        self.journey_date = journey_date
        self.flight_time = flight_time
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.booking_id = booking_id
        self.travel_ticket = travel_ticket
        self.food_bill = food_bill
        self.snacks_bill = snacks_bill

    def total_bill(self):
        return self.travel_ticket + self.food_bill + self.snacks_bill

    def print_ticket(self):
        print("\n--- FLIGHT TICKET ---\n")
        print(f"Airlines Travel Name : {self.name_airlines}")
        print(f"Passenger Name       : {self.name_passenger}")
        print(f"Journey Date         : {self.journey_date}")
        print(f"Flight Time (IST)    : {self.flight_time}")
        print(f"Starting Point       : {self.starting_point}")
        print(f"Ending Point         : {self.ending_point}")
        print(f"Booking ID           : {self.booking_id}")
        print(f"Total Bill Amount    : ₹{self.total_bill():.2f}")
        print("\n*** Thank You For Choosing Us ***\n")


# Creating object (same values from your C code)

ticket = Airlines(
    "SpiceJet",
    "SahanaaMR",
    "25.10.2026",
    "18:00pm IST",
    "CHENNAI",
    "PARIS",
    "25010059434210",
    18000.0,
    1000.0,
    500.0
)

ticket.print_ticket()
