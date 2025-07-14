import csv
import uuid
import sys


def main():
    print("Welcome to the cinema booking system")
    print("Select an option below to continue")
    print("Press 1 to book a film")
    print("Press 2 to search by film name")
    print("Press 3 to search by booking reference")
    choice = input("Please select an option: ")

    if choice == "1":
        new_booking = addbooking()
        print("Thank you, your booking reference is:", new_booking)

    elif choice == "2":
        result = searchfilm()
        if result:
            print(result)
        else:
            print("No film found")
            sys.exit(1)

    elif choice == "3":
        result = searchref()
        if result:
            print(result)
        else:
            print("No reference found")
            sys.exit(1)
    else:
        print("Invalid entry")
        sys.exit(1)

def addbooking():
    bookings = []
    data = []
    with open("cinema.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    new_uuid = uuid.uuid4().hex[:8]
    col0 = [x[0] for x in data]
    while new_uuid in col0:
        new_uuid = uuid.uuid4().hex

    bookings.append(new_uuid)

    while True:
        surname = input("Please enter your surname: ").lower().strip()
        if surname:
            break
        else:
            print("Surname cannot be empty.")
    bookings.append(surname)

    while True:
        forename = input("Please enter your forename: ").lower().strip()
        if forename:
            break
        else:
            print("Forename cannot be empty.")
    bookings.append(forename)

    films = ['dune', 'trainspotting', "frozen", "hercules", "mission impossible", "trollhunter", "kill buljo",]
    while True:
        film = input("Please enter the film you want to see: ").lower().strip()
        if film in films:
            break
        else:
            print("Film name cannot be empty.")
    bookings.append(film)

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("What day of the week do you want to see the film?: ").lower().strip()
        if day in days:
            break
        else:
            print("Please enter a valid day of the week.")
    bookings.append(day)
    with open("cinema.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(bookings)

    return new_uuid

def searchfilm():
    data = []
    with open("cinema.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    lookup = input("Please enter a film name: ").lower()
    col4 = [x[3] for x in data]
    if lookup in col4:
        results = []
        for k in range(0, len(col4)):
            if col4[k] == lookup:
                results.append(data[k])
        return results
    else:
        return None


def searchref():
    data = []
    with open("cinema.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    lookup = input("Please enter a booking reference: ")
    col1 = [x[0] for x in data]
    if lookup in col1:
        for k in range(0, len(col1)):
            if col1[k] == lookup:
                return data[k]
    else:
        return None


if __name__ == "__main__":
    main()