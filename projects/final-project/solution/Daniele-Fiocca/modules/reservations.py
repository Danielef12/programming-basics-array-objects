from projection import display_projections, load_projections, save_projections


def add_reservations():
    reservation_list = load_projections()
    while True:
        name = input("What is your name? ").strip()
        if name:
            break
        print("Name must not be empty.")

    display_projections()

    film_selection = int(input("Select the number of the movie to reserve seats: ")) - 1
    if not (0 <= film_selection < len(reservation_list)):
        print("Invalid selection")
        return

    selected_movie = reservation_list[film_selection]

    while True:
        try:
            seats = int(input("Insert the number of seats: "))

            if seats <= 0:
                print("You must select at least one seat")
                return
            if seats > selected_movie["available_seats"]:
                print("Not enough available seats")
                return
            else:
                break
        except ValueError:
            print("Invalid number of seats")

    selected_movie["reserved"].append({"name": name, "seats": seats})
    selected_movie["available_seats"] -= seats

    save_projections(reservation_list)
    print(
        f"reservation confirmed for {name}: {seats} seats for {selected_movie['title']}"
    )


def find_reservations_by_name(reservation_list, name):
    name = name.strip().lower()
    matched_reservations = []
    for movie in reservation_list:
        for i, reservation in enumerate(movie["reserved"]):
            if reservation["name"].lower() == name:
                matched_reservations.append((movie, i, reservation))
    return matched_reservations


def choose_reservation_from_match(name, matched_reservations):
    print(f"Found {len(matched_reservations)} reservations for '{name}':")
    for list_count, (movie, i, reservation) in enumerate(matched_reservations, start=1):
        print(
            f"{list_count}. Movie: {movie['title']} at {movie['time']} in {movie['theater']} - Seats: {reservation['seats']}"
        )

    choice = input("Select reservation: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(matched_reservations)):
        print("Invalid selection")
        return None, None, None

    return matched_reservations[int(choice) - 1]


def modify_reservations():
    reservation_list = load_projections()
    name = input("Enter the name used for the reservation: ").strip()
    matched_reservations = find_reservations_by_name(reservation_list, name)

    if not matched_reservations:
        print("No reservations found")
        return

    movie, index, reservation = choose_reservation_from_match(
        name, matched_reservations
    )
    if not reservation:
        return

    try:
        new_seats = int(input("Enter the new number of seats: "))
        if new_seats <= 0:
            print("You must select at least one seat")
            return

        seat_difference = new_seats - reservation["seats"]

        if movie["available_seats"] - seat_difference < 0:
            print("Not enough available seats")
            return

        movie["available_seats"] -= seat_difference
        reservation["seats"] = new_seats
        save_projections(reservation_list)
        print("Reservation update confirmed")
        return

    except ValueError:
        print("Invalid number.")
        return


def delete_reservations():
    reservation_list = load_projections()
    name = input("Enter the name used for the reservation: ").strip()
    matched_reservations = find_reservations_by_name(reservation_list, name)
    if not matched_reservations:
        print("No reservations found")
        return

    movie, index, reservation = choose_reservation_from_match(
        name, matched_reservations
    )
    if not reservation:
        return

    confirm = input("Would you like to delete the reservation? (y/n): ").lower()
    if confirm == "y":
        movie["reserved"].remove(reservation)
        movie["available_seats"] += reservation["seats"]
        print("Saving this to file:", reservation_list)
        save_projections(reservation_list)
        print(f"Reservation deleted")
    else:
        print("Reservation not deleted")
    return
