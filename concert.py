"""
Author: Fearghal Hayes
Description: This program helps to organize the Blackwater Annual Concert.
"""


def get_integer_input(prompt, error_message="Invalid input. Please try again.", condition=lambda x: True):
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def add_performer(performers):
    print("\nAdding Performers")
    performer_count = get_integer_input("How many performers are you adding? ==> ",
                                        "Please enter a positive number.",
                                        lambda x: x > 0)
    with open("performer.txt", "a") as file:  # Open the file in append mode
        for i in range(performer_count):
            firstname = input("Enter your firstname (No Commas): ==> ").strip()
            surname = input("Enter your surname (No Commas): ==> ").strip()
            performance_type = get_integer_input("\nEnter your type of Performance:\n1. Musical\n2. Singer\n3. "
                                                 "Dance\n==> ",
                                                 "Choose a valid option: 1, 2, or 3.",
                                                 lambda x: 1 <= x <= 3)
            performance_type_str = ["Musician", "Singer", "Dancer"][performance_type-1]
            performance_duration = get_integer_input("Please enter how long your act is (In minutes): ==> ",
                                                     "Enter a positive number for minutes.",
                                                     lambda x: x > 0)
            performers.append((firstname, surname, performance_type_str, performance_duration))
            # Write to file with the specified format
            file.write(f"{i+1},{firstname},{surname},{performance_type_str},{performance_duration}\n")


def generate_concert_details(performers):
    print("\nConcert Details\n" + "-" * 20)
    for i, (firstname, surname, performance_type, duration) in enumerate(performers, start=1):
        star = "*" if duration > 15 else ""
        print(f"{i}: {firstname} {surname}{star}\t({performance_type})\t{duration} Minutes")
    print("-" * 20)


def main():
    performers = []
    while True:
        print("\nWelcome to Fearghal's Blackwater Concert Organiser (BCO)!")
        choice = get_integer_input(
            "1. Adding Performers\n2. Generate Concert Details\n3. Quit\nPlease enter an option ==> ",
            "Choose between 1 and 3.",
            lambda x: 1 <= x <= 3)
        if choice == 1:
            add_performer(performers)
        elif choice == 2:
            generate_concert_details(performers)
        elif choice == 3:
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()
