#UNWSP Programming PythonCos2005DEsp25
#Program_2_Cities_db_Interactions
#05.02.25
#Abraham. N. Andersen

import sqlite3

def display_cities(cursor, order_by=None, sort_order="ASC"):
    """Displays a list of cities, optionally sorted."""
    sql = "SELECT CityName, Population FROM Cities"
    if order_by:
        sql += f" ORDER BY {order_by} {sort_order}"
    cursor.execute(sql)
    cities = cursor.fetchall()
    if cities:
        print("\nCity Name             Population")
        print("---------------------- ----------")
        for city, population in cities:
            print(f"{city:<22} {population:,.0f}")
    else:
        print("No cities found.")

def display_total_population(cursor):
    """Displays the total population of all cities."""
    cursor.execute("SELECT SUM(Population) FROM Cities")
    total_population = cursor.fetchone()[0]
    if total_population is not None:
        print(f"\nTotal Population of all cities: {total_population:,.0f}")
    else:
        print("No population data available.")

def display_average_population(cursor):
    """Displays the average population of all cities."""
    cursor.execute("SELECT AVG(Population) FROM Cities")
    average_population = cursor.fetchone()[0]
    if average_population is not None:
        print(f"\nAverage Population of all cities: {average_population:,.0f}")
    else:
        print("No population data available.")

def display_city_with_highest_population(cursor):
    """Displays the city with the highest population."""
    cursor.execute("SELECT CityName, MAX(Population) FROM Cities")
    result = cursor.fetchone()
    if result:
        print(f"\nCity with the Highest Population: {result[0]} ({result[1]:,.0f})")
    else:
        print("No city data available.")

def display_city_with_lowest_population(cursor):
    """Displays the city with the lowest population."""
    cursor.execute("SELECT CityName, MIN(Population) FROM Cities")
    result = cursor.fetchone()
    if result:
        print(f"\nCity with the Lowest Population: {result[0]} ({result[1]:,.0f})")
    else:
        print("No city data available.")

def main():
    # Connect to db.
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    while True:
        print("\nSelect an operation:")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display the total population of all cities")
        print("5. Display the average population of all cities")
        print("6. Display the city with the highest population")
        print("7. Display the city with the lowest population")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            display_cities(cur, order_by='Population', sort_order='ASC')
        elif choice == '2':
            display_cities(cur, order_by='Population', sort_order='DESC')
        elif choice == '3':
            display_cities(cur, order_by='CityName')
        elif choice == '4':
            display_total_population(cur)
        elif choice == '5':
            display_average_population(cur)
        elif choice == '6':
            display_city_with_highest_population(cur)
        elif choice == '7':
            display_city_with_lowest_population(cur)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    conn.close()

if __name__ == "__main__":
    main()