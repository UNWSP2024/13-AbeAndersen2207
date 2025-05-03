#UNWSP Programming PythonCos2005DEsp25
#Program_4_Phonebook_db_Interactions
#05.02.25
#Abraham. N. Andersen

import sqlite3

def add_entry(cursor, name, phone_number):
    """Adds a new entry to the phone book."""
    try:
        cursor.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone_number))
        print(f"Entry for '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: '{name}' already exists in the phone book.")

def lookup_number(cursor, name):
    """Looks up a phone number by name."""
    cursor.execute("SELECT PhoneNumber FROM Entries WHERE Name = ?", (name,))
    result = cursor.fetchone()
    if result:
        print(f"The phone number for '{name}' is: {result[0]}")
    else:
        print(f"'{name}' not found in the phone book.")

def change_number(cursor, name, new_phone_number):
    """Changes the phone number for a given name."""
    cursor.execute("UPDATE Entries SET PhoneNumber = ? WHERE Name = ?", (new_phone_number, name))
    if cursor.rowcount > 0:
        print(f"Phone number for '{name}' updated successfully to '{new_phone_number}'.")
    else:
        print(f"'{name}' not found in the phone book.")

def delete_entry(cursor, name):
    """Deletes an entry from the phone book."""
    cursor.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    if cursor.rowcount > 0:
        print(f"Entry for '{name}' deleted successfully.")
    else:
        print(f"'{name}' not found in the phone book.")

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    while True:
        print("\nPhone Book Application:")
        print("1. Add New Entry")
        print("2. Look Up Number")
        print("3. Change Number")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_entry(cur, name, phone)
            conn.commit()
        elif choice == '2':
            name = input("Enter name to look up: ")
            lookup_number(cur, name)
        elif choice == '3':
            name = input("Enter name to change number for: ")
            new_phone = input("Enter the new phone number: ")
            change_number(cur, name, new_phone)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_entry(cur, name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        conn.commit()  #Save changes after each operation

    conn.close()

if __name__ == "__main__":
    main()