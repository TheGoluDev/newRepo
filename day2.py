seats = {
    "seat_1": "NOT_BOOKED",
    "seat_2": "NOT_BOOKED",
    "seat_3": "NOT_BOOKED",
    "seat_4": "NOT_BOOKED",
    "seat_5": "NOT_BOOKED",
    "seat_6": "NOT_BOOKED",
    "seat_7": "NOT_BOOKED"
}

while True:
    print("\n\n\nAvailable seats:")
    for seat, status in seats.items():
        print(f"{seat}: {status}")

    seat_no = input("\nEnter the seat no you want to book (or type 'exit' to quit): ").strip().lower()

    if seat_no == 'exit':
        print("Thank you for using the bus booking system!")
        break

    seat_key = seat_no if seat_no.startswith("seat_") else f"seat_{seat_no}"

    if seat_key in seats:
        if seats[seat_key] == "NOT_BOOKED":
            seats[seat_key] = "BOOKED"
            print(f"{seat_key} has been successfully booked!")
        else:
            print(f"{seat_key} is already booked!")
    else:
        print("Invalid seat number. Please try again.")