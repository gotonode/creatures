import sys  # Needed to gracefully quit the Python app.

__DEFAULT_DATABASE_FILE__ = "database.txt"

# We call these "creatures" because Python doesn't like the 'é' in Pokémon.
creatures = []  # We store all the Pokémon here.


def add_creature():
# Creates a new Pokémon based on user-given data, and adds it to the list.

    creature = {}

    while True:
        id = input("ID: ").strip()

        # This checks that the given value is an integer.
        try:
            id_for_check = int(id)
            if id_for_check <= 0:
                print("Please give a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")

    creature["id"] = id

    while True:
        name = input("Name: ").strip()

        if len(name) == 0:
            print("Please enter a name for the Pokémon.")
        else:
            break

    creature["name"] = name

    while True:
        type1 = input("Main type: ").strip()

        if len(type1) == 0:
            print("Please enter a main (primary) type for the Pokémon.")
        else:
            break

    creature["type1"] = type1

    type2 = input("Secondary type (leave blank for none): ").strip()
    creature["type2"] = type2

    while True:
        caught = input("Have you caught this Pokémon [Y/N]? ").strip().upper()
        if caught == "Y" or caught == "N":
            break
        else:
            print("Please either enter 'Y' for yes or 'N' for no.")

    creature["caught"] = caught

    creatures.append(creature)  # Append the new creature to the list of all creatures.

    print("Pokémon has been created and added to the in-memory database.")
    print("Please remember to save your changes.")
    print()


def find_creature():
# Used to find a Pokémon, by ID or by name. Returns None if it can't find one.

    prompt = input("Please enter the Pokémon's name or ID: ").strip()
    creature = None
    try:
        id = int(prompt)
        # This worked, so it is an integer (i.e., an ID).
        creature = find_creature_by_id(id)
    except ValueError:
        # This did not work, so it must be the Pokémon's name.
        name = prompt
        creature = find_creature_by_name(name)

    return creature  # Returns the found Pokémon, or None.


def edit_creature():
# Edit's a Pokémon's caught-status, if that Pokémon is found.

    creature = find_creature()

    if not creature:
        print("Could not find a Pokémon by that name or ID, so can't make changes to it.")
        print()
        return

    while True:
        caught = input("Have you caught this Pokémon [Y/N]? ").strip().upper()
        if caught == "Y" or caught == "N":
            break
        else:
            print("Please either enter 'Y' for yes or 'N' for no.")

    creature["caught"] = caught

    print("Pokémon has been updated.")
    print()


def remove_creature():
# Removes a Pokémon from the database, if found.

    creature = find_creature()

    if not creature:
        print("Could not find a Pokémon by that name or ID, so can't remove it.")
        print()
        return

    creatures.remove(creature)

    print("Pokémon removed.")
    print()


def list_creatures():
# Lists all the Pokémon in the database.

    if len(creatures) == 0:
        print("No Pokémon in the database. Perhaps you'd like to load a database or add a new Pokémon?")
        print()
        return

    print("Would you like your Pokémon sorted by their ID (1), name (2), primary type (3) or secondary type (4)?")

    while True:
        choice = input("Please enter your choice (an integer): ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                print("Please give a valid choice (1-4).")
            else:
                break

        except ValueError:
            print("That wasn't an integer.")

    new_list = []  # This is the new, sorted list.

    if choice == 1:
        # We sort by ID (an integer).
        new_list = sorted(creatures, key = lambda k: int(k["id"]), reverse=False)
    else:
        # We sort by a string (not an integer).
        if choice == 2:
            sort_by = "name"
        elif choice == 3:
            sort_by = "type1"
        else:
            sort_by = "type2"

        new_list = sorted(creatures, key = lambda k: k[sort_by], reverse=False)

    print("Here are your Pokémon: ")

    for creature in new_list:
        type = creature["type1"]
        if len(creature["type2"]) > 0:
            # If it has two types, they will be displayed nicely.
            type = type + " / " + creature["type2"]

        if creature["caught"] == "Y":
            caught = ", caught"
        else:
            caught = ", not caught yet"

        print(creature["id"] + ". " + creature["name"] + " (" + type + ")" + caught)

    print()


def find_creature_by_name(name):
# Finds a Pokémon by name, returns None otherwise.

    for creature in creatures:
        if creature["name"].lower() == name.lower():
            return creature
    return None


def find_creature_by_id(id):
# Finds a Pokémon by ID, returns None otherwise.

    for creature in creatures:
        if int(creature["id"]) == id:
            return creature
    return None


def print_instructions():
# These instructions are printed when the app is first run, and subsequently only when requested.

    print("Please choose a command")
    print()  # To me, these are more readable than using "\n". Case-dependent, of course.
    print("A: Add a new Pokémon")
    print("R: Remove an existing Pokémon")
    print("E: Edit an existing Pokémon")
    print("L: List all Pokémon (list order will be asked)")
    print()
    print("1: Load the database from an existing file (clears the memory)")
    print("2: Save the database to a file")
    print()
    print("3: Quit the app")
    print()


def exit_app():
# This quits the app.

    print("Thanks for browsing the Pokémon database. App terminated.")
    print()
    sys.exit()


def save_database():
# Here we ask the user for the database file name, and then save each Pokémon on its own row (entry).

    file_name = input("Where to save the database (default '" + __DEFAULT_DATABASE_FILE__ + "'): ").strip()

    if len(file_name) == 0:
        file_name = __DEFAULT_DATABASE_FILE__

    try:
        file = open(file_name, "wt")  # Write, text.
    except IOError:
        print("Couldn't save to that database.")
        return

    for creature in creatures:
        # Ineffective for large amounts of data, but pretty to look at.
        entry = creature["id"] + "|"
        entry = entry + creature["name"] + "|"
        entry = entry + creature["type1"] + "|"
        entry = entry + creature["type2"] + "|"
        entry = entry + creature["caught"]
        entry = entry + "\n"

        # Sample data:
        # 1|Bulbasaur|Grass||N
        # 6|Charizard|Fire|Flying|N
        # 25|Pikachu|Eletric||Y
        #
        # Each row contains exactly four (4) pipe characters, even if the space between them contains nothing.

        file.write(entry)

    file.close()

    print("Database written successfully to '" + file_name + "'.")
    print()


def load_database():
# After the user has given the database file name, we'll loop through all rows and create new Pokémon based on them.

    file_name = input("Which database to load (default '" + __DEFAULT_DATABASE_FILE__ + "'): ").strip()

    if len(file_name) == 0:
        file_name = __DEFAULT_DATABASE_FILE__

    try:
        file = open(file_name, "rt")  # Read, text.
    except IOError:
        print("Couldn't open that database.")
        return

    creatures.clear()  # We empty the existing data.

    for row in file:
        data = row.split("|")  # Split based on the pipe ('|') character.
        creature = {}
        creature["id"] = data[0]
        creature["name"] = data[1]
        creature["type1"] = data[2]
        creature["type2"] = data[3]
        creature["caught"] = data[4]

        creatures.append(creature)

    file.close()

    print("Database loaded successfully.")
    print()


def loop_program():
# The main loop for the program. Will never end, unless explicitly asked to do so.

    command = input("Command ('X' for list of commands): ").strip().upper()  # We put it uppercase just in case.
    if command == "X":
        print()
        print_instructions()
    elif command == "L":
        print()
        list_creatures()
    elif command == "E":
        print()
        edit_creature()
    elif command == "A":
        print()
        add_creature()
    elif command == "R":
        print()
        remove_creature()
    elif command == "2":
        print()
        save_database()
    elif command == "1":
        print()
        load_database()
    elif command == "3":
        print()
        exit_app()
    else:
        print("Unknown command. Type 'X' to see the list of available commands.")
        print()

# Here the app starts, after it has been defined in whole.

print("Welcome to the Pokémon Database!")
print()
print_instructions()

while True:
    loop_program()
