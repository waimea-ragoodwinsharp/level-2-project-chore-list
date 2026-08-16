#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------
class PeopleTable:

    NAME = "person"

    SCHEMA = """
        CREATE TABLE person (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            
        )
    """
 SEED_DATA = """
        INSERT INTO note (id, name)
        VALUES
            ("4",  "Rose"),
            ("5",  "James"),
            ("2",  "Jeremy")
           
    """


class ChoreTable:

    NAME = "chores"

    SCHEMA = """
        CREATE TABLE chores (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            person_id    TEXT,
            priotiy  INTEGER DEFAULT 0,
            due TEXT,
            repeat BOOLEAN,
            done BOOLEAN
        )
    """
 SEED_DATA = """
        INSERT INTO note (name, person_id, priority, due, repeat, done)
        VALUES
            ("Vacuum",      "4", "3", "7/11/2026", "No repeat", "1"),
            ("Clean Chickens",  "5", "2", "12/12/2026", "Repeat every day", "0"),
            ("cook dinner",  "2", "2", "30/3/2026", "repeat daily", "0")
           
    """



#class NoteTable:

#    NAME = "note"

 #   SCHEMA = """
 #       CREATE TABLE note (
 #           id      INTEGER PRIMARY KEY AUTOINCREMENT,
 #           title   TEXT NOT NULL,
 #           body    TEXT,
 #           pinned  INTEGER DEFAULT 0,
#            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#        )
 #   """
#
 #   SEED_DATA = """
#        INSERT INTO note (title, pinned, body)
 #       VALUES
 #           ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
#            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
 #           ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
#            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
 #           ("Important!",    1, "Remember to backup your database regularly.")
#    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     PeopleTable,
#     ChoreTable
#    
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    NoteTable,
    # Add more tables here...
]

