# Pokémon Database

This is the accompanied documentation for the Pokémon Database Python app.

## Case & functionality

When the app is launched, it presents the user with all available commands. The user chooses a command by typing it in and pressing [RETURN]. The commands are single-character, such as 1 or A. For letters, it doesn't matter if the user types it in lowercase or uppercase, the app changes them all to uppercase.

The user can now choose to add a Pokémon, "Pikachu". Choosing option 'A' to add it, the system asks for the new Pokémon's information. First, the user enters its ID (in this case, 25) and the system verifies that it is a positive integer. After that, the Pokémon's name is given ("Pikachu"), then its main type ("eletric") and a secondary type (this is optional). Finally, the user indicates via a 'Y' or 'N' if he/she has caught that Pokémon (in whatever game this app is used for, be it Pokémon Red/Blue for the GameBoy or Pokémon GO for Android, as an example). This user has not yet caught Pikachu.

To view a list of all the Pokémon in the database, the user can choose from four different ordering options. An existing Pokémon can also be removed. And once a Pokémon has been caught, or returned to the wild, it's caught-status can be changed via the 'E' command. A Pokémon who is to be removed/edited must be indicated by either its ID or name. It doesn't matter if the search term is all in lowercase; this app will find the Pokémon nonetheless.

Once Pokémon have been added/removed/edited, they can be saved via the '1' command. The user can define the path and filename of the database to be used. When restoring data, command '2' is used and again, the path and filename can be specified. In both of these cases, if nothing is defined, the default value of "database.txt" is used.

Finally, the user can exit the app with the '3' command.

## Database

Pokémon Database uses a simple text file as its database. A file of any extension can be used, and the app suggests a default name of "database.txt" for simplicity.

Each row in the plaintext database file is an entry on its own. An entry is a specific Pokémon, and contains the following information:

- Pokémon's ID, an integer (this should be unique)
- Pokémon's name (also unique)
- Main type (mandatory)
- Secondary type (this can be blank)
- Information whether the user has caught this Pokémon (either a 'Y' or a 'N')

The data is split with the pipe character ('|') in the text file. Here are a few example rows (entries):

- `1|Bulbasaur|Grass|Poison|N`
- `6|Charizard|Fire|Flying|N`
- `25|Pikachu|Eletric||Y`

The empty space between the last two pipe characters is the place where the Pokémon's secondary type would be placed. But in the case of its absence, the number of pipes is still the same. So every row consists of exactly four (4) of these pipe characters.

A sample database can be found here: [database.txt](https://github.com/gotonode/creatures/blob/master/database.txt)

The user can add a Pokémon, view a list of all the Pokémon in the database (with different sorting options), edit the caught-status of the Pokémon, and remove a Pokémon. The database can also be saved and loaded. A custom file can be defined as the source/target for the database.

I chose to use Python's dictionary-based approach because that was new to me. Immediately I wanted to make it more object-based, in that I would've created a new object called Pokémon and then create, store, edit and delete these objects in a list. But this was a good learning experience, and really showed why Python is used in so many science/tech fields.

The double empty spaces before each function ("def") is a Python convention. Same goes for double spaces before the hash symbol ('#') on single-line comments after code. Comments which are on their own line do not begin with any spaces before them.

## Functions (methods)

Many functions were created to avoid repetition ("DRY"). In Python, a function is defined with the "def" keyword. Each function has been commented, and named appropriately. Please refer to the code for more information.

Here's a list of all the functions and their uses in this app:

- "`add_creature`" creates a new Pokémon and adds it to the list
- "`ask_if_caught`" is used when creating a new Pokémon and when editing an existing one
- "`find_creature`" finds a Pokémon by its ID (integer) or name (string)
- "`edit_creature`" changes the caught-status of the Pokémon
- "`remove_creature`" removes a single Pokémon, based on its ID or name
- "`list_creatures`" lists all the Pokémon in the database in one of four different ways
- "`find_creature_by_name`" is a helper function which does what the name suggests, returns None otherwise
- "`find_creature_by_id`" is the same as above, but an ID is used instead of name
- "`print_instructions`" prints to the console all the available commands
- "`save_database`" saves the in-memory database to a file (which can be defined)
- "`load_database`" clears the memory and loads Pokémon from a database file
- "`exit_app`" is used to exit the app
- "`loop_program`" loops the program indefinitely, until asked to exit

## Technical

Input validation is performed in an infinite loop which exists (break) only when the input is deemed valid. For an example, if a positive integer is needed, it firsts checks if it is an integer in the first place, then compares it to zero (it must be greater than). Only when 1 (or higher than 1) is entered as input does the loop end. Drawback here is that the user has no way of exiting and returning to the main menu, if he/she would like to abort the operation.

When the user wishes to view a list of his/her Pokémon, four sorting choices are available:

1. Sort by ID
2. Sort by name
3. Sort by primary type
4. Sort by secondary type

## Flaws in the system

A few flaws have been identified. These could also be called shortcomings.

If the Pokémon's name or type (primary/secondary) contains the pipe character ('|'), then it would break the database and most likely crash the app. So far, no Pokémon have been named this way, and it is unlikely to happen. This is why the pipe character was chosen as the delimiter. But this doesn't prevent the user from adding data that contains it. Manually editing the database file with ignorance can also cause problems.

When opening a database (file), the app empties the list of existing Pokémon. For production use, a check should be performed if the user wants to load a new database when existing, modified data would be destroyed.

When changes have been made, and the app is asked to close, it should ask the user if he/she wants to save the changes made to the data prior to closing down.

Upon adding new Pokémon to the system, checks should be made if an ID/name already exists in the database. Should we allow more than one Pokémon of the same ID and/or name to be added?
