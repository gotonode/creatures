# Pokémon Database

This is the accompanied documentation for the Pokémon Database Python app.

Pokémon Database uses a simple text file as its database. A file of any extension can be used, and the app suggests a default name of "database.txt" for simplicity.

Each row in the plaintext database file is an entry on its own. An entry is a specific Pokémon, and contains the following information:

- Pokémon's ID, an integer (this should be unique)
- Pokémon's name (also unique)
- Main type (mandatory)
- Secondary type (this can be blank)
- Information whether the user has caught this Pokémon (either a 'Y' or a 'N')

The data is split with the pipe character ('|') in the text file. Here are a few example rows (entries):

- 1|Bulbasaur|Grass||N
- 6|Charizard|Fire|Flying|N
- 25|Pikachu|Eletric||Y

The empty space between the last two pipe characters is the place where the Pokémon's secondary type would be placed. But in the case of its absence, the number of pipes is still the same. So every row consists of exactly four (4) of these pipe characters.

A sample database can be found here: [database.txt](https://github.com/gotonode/creatures/blob/master/database.txt)

I chose to use Python's dictionary-based approach because that was new to me. Immediately I wanted to make it more object-based, in that I would've created a new object called Pokémon and then create, store, edit and delete these objects in a list. But this was a good learning experience, and really showed why Python is used in so many science/tech fields.

The double empty spaces before each function ("def") is a Python convention. Same goes for double spaces before the hash symbol ('#') on single-line comments after code. Comments which are on their own line do not begin with any spaces before them.

Many functions were created to avoid repetition ("DRY").

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
