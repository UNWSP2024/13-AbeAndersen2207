#UNWSP Programming PythonCos2005DEsp25
#Program_3_Phonebook_db
#05.02.25
#Abraham. N. Andersen

#This is my own code...

import sqlite3

def create_phonebook_db():
    """Creates the phonebook.db database and the Entries table."""
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    Name TEXT PRIMARY KEY,
                    PhoneNumber TEXT
                )''')
    conn.commit()
    conn.close()
    print("phonebook.db database and Entries table created successfully!")

if __name__ == "__main__":
    create_phonebook_db()


