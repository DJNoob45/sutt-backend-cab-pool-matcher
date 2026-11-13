from models import RideRequest, Cab, CITIES, SLOTS

waiting = []
cabs = []
def ask_name():
    while True:
        name = input("Student name: ").strip()
        if name != "":
            return name
        print("Name cannot be empty.")


def ask_choice(question, options):
    while True:
        answer = input(question + " (" + "/".join(options) + "): ").strip().title()
        if answer in options:
            return answer
        print("Sorry, please choose one of:", ", ".join(options))


def ask_year():
    while True:
        text = input("Year (1 to 5): ").strip()
        if text.isdigit() and 1 <= int(text) <= 5:
            return int(text)
        print("Year must be a number from 1 to 5.")


def add_request():
    name = ask_name()
    city = ask_choice("Destination", CITIES)
    slot = ask_choice("Time slot", SLOTS)
    year = ask_year()

    request = RideRequest(name, city, slot, year)
    waiting.append(request)
    print("Request added. You are now waiting for", city, slot)


def show_waiting():
    print(" Waiting students")
    if len(waiting) == 0:
        print("Nobody is waiting.")
    for r in waiting:
        print(f"{r.name} | Year {r.year} | {r.city} {r.slot}")


def show_cabs():
    print(" Cabs ")
    if len(cabs) == 0:
        print("No cabs loaded.")
    for cab in cabs:
        if cab.left:
            status = "Left"
        else:
            status = "Open"
        print(f"{cab.driver} | {cab.city} {cab.slot} | {len(cab.students)}/{cab.seats} | {status}")
        for s in cab.students:
            print("    -", s.name, "(Year", s.year, ")")



while True:
    print()
    print("1. Add ride request")
    print("2. Show waiting students and cabs")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        add_request()
    elif choice == "2":
        show_waiting()
        show_cabs()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Please enter 1, 2 or 3.")