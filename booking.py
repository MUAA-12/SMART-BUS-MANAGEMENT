from data import routes, bookings, booking_ids

def view_routes():
    print("\n==========Available Bus Routes===========")
    for number,route in enumerate(routes,start=1):
        print(f"\nBus Number: {number}")
        print(f"Route ID:{route['route_id']}")
        print(f"departure_city:{route['departure_city']}")
        print(f"destination_city:{route['destination_city']}")
        print(f"departure_time:{route['departure_time']}")
        print(f"ticket_price:{route['ticket_price']}")
        print(f"total_seats:{route['total_seats']}")
        print(f"available_seats:{route['available_seats']}") 

def search_routes():

    departure = input("enter your departure city:")
    destination = input("Enter your Destination city:")

    for route in routes:
        if departure.lower() == route["departure_city"].lower() and destination.lower() == route["destination_city"].lower():
            print(f"Departure city :{route['departure_city']}")
            print(f"Destination city :{route['destination_city']}")
            break
    else:
        print("No Route Found")

def book_ticket():

    route_id = input("Enter your Route_ID:").strip().upper()
    for route in routes:
        if route['route_id'] == route_id:
            passenger_name = input("Enter your name:").strip()
            passenger_age  = int(input("Enter your age:"))
            seats_requested = int(input("Enter your requested seats:"))
            if seats_requested > route['available_seats']:
                print("Not Enough seats available!")
                return
            elif seats_requested <= 0:
                print("Invalid Number")
                return
            total_fare = route['ticket_price']*seats_requested
            booking_id = f"B{len(bookings) + 1:03d}"
            booking = {
                "booking_id" : booking_id,
                "passenger_name":passenger_name,
                "passenger_age":passenger_age,
                "route_id":route_id,
                "seats_booked":seats_requested,
                "total_fare":total_fare,
                "status":"Confirmed"
            }
            bookings.append(booking)
            booking_ids.add(booking_id)
            route['available_seats'] -= seats_requested
            print("\n========== BOOKING CONFIRMED ==========")
            print(f"Booking ID: {booking_id}")
            print(f"Passenger: {passenger_name}")
            print(f"Route ID: {route_id}")
            print(f"Seats Booked: {seats_requested}")
            print(f"Total Fare: Rs. {total_fare}")
            print("Status: Confirmed")
            break
        
def view_bookings():
    booking_id = input("Enter your booking_id:").strip().upper()

    for booking in bookings:
        if booking_id == booking['booking_id']:
            print("Booking found!")
            print(f"Passenger Name: {booking['passenger_name']}")
            print(f"Passenger Age : {booking['passenger_age']}")
            print(f"Route ID:{booking['route_id']}")
            print(f"Seats booked : {booking['seats_booked']}")
            print(f"Total fare : {booking['total_fare']}")
            print(f"status:{booking['status']}")
            break
    else:
        print("Booking not found")

def cancel_booking():
    booking_id = input("Enter booking ID to cancel:").strip().upper()

    for booking in bookings:
        if booking['booking_id'] == booking_id:
            if booking['status'] == "Cancelled":
                print("This booking is already Cancelled")
                return

            for route in routes:
                if route['route_id'] == booking['route_id']:
                    route['available_seats'] += booking['seats_booked']
                    booking['status'] = "Cancelled"
                    print(f"Booking {booking_id} cancelled successfully!")
                    return
            print("booking route not found")
            return
    else:
        print("Booking Not Found!")

def view_seat_availability():
    route_id = input("Enter Route ID: ").strip().upper()

    for route in routes:
        if route['route_id'] == route_id:
            booked_seats = route['total_seats'] - route['available_seats']

            print(f"Route ID: {route['route_id']}")
            print(f"Total Seats: {route['total_seats']}")
            print(f"Available Seats: {route['available_seats']}")
            print(f"Booked Seats: {booked_seats}")
            return

    print("Route Not Found!")

def generate_booking_report():
    total_bookings = 0
    total_seats = 0
    total_revenue = 0

    for booking in bookings:
        if booking['status'] == "Confirmed":
            total_bookings += 1
            total_seats += booking['seats_booked']
            total_revenue += booking['total_fare']

    print("\n========== BOOKING REPORT ==========")
    print(f"Total Confirmed Bookings: {total_bookings}")
    print(f"Total Seats Booked: {total_seats}")
    print(f"Total Revenue: Rs. {total_revenue}")