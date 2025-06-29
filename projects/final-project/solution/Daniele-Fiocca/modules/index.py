from projection import display_projections
from reservations import add_reservations, delete_reservations, modify_reservations


def display_menu():
    print("Cinema Booking Manager")
    print("1. Display cinema projection program")
    print("2. Booking a projection.")
    print("3. Modification of reservation.")
    print("4. Delete reservation.")
    print("5. Exit")


def selection_program():
    while True:
        display_menu()
        try:
            selection = int(input("Enter a selection: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        match selection:
            case 1:
                display_projections()
            case 2:
                add_reservations()
            case 3:
                modify_reservations()
            case 4:
                delete_reservations()
            case 5:
                print("Thank you for using the Cinema Booking Manager!")
                break
            case _:
                print("Invalid selection. Try again.")


def main():
    selection_program()
