# SMART BUS RESERVATION SYSTEM
from booking import view_routes,search_routes , book_ticket, view_bookings, cancel_booking, view_seat_availability, generate_booking_report

while (True):
    print("""
           1. View Available Routes
           2. Search for a Route
           3. Book a Ticket
           4. View My Bookings
           5. Cancel a Booking
           6. View Seat Availability
           7. Generate Booking Report
           8. Exit
    """)

    choice = input("Enter your choice:")

    if choice == "1":
        print("View Available Routes")
        view_routes()

    elif choice == "2":
        print("Search for a Route")
        search_routes()

    elif choice == "3":
        print("Book a Ticket")
        book_ticket()

    elif choice == "4":
        print("View My Bookings")
        view_bookings()

    elif choice == "5":
        print("Cancel a Booking")
        cancel_booking()

    elif choice == "6":
        print("View Seat Availability")
        view_seat_availability()

    elif choice == "7":
        print("Generate Booking Report")
        generate_booking_report()

    elif choice == "8":
        print("Thank for using Smart Bus")
        break
    else:
        print("InValid Choice")
    


 
