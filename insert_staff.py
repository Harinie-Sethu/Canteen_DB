import mysql.connector
from mysql.connector import Error

# Function to establish a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="CANTEEN"
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to insert data into the STAFF table
def insert_into_staff(cursor, staff_id, salary, super_staff_id, canteen_id, aadhar):
    try:
        cursor.execute(
            "INSERT INTO STAFF (StaffID, Salary, SuperStaffID, CanID, Aadhar) VALUES (%s, %s, %s, %s, %s)",
            (staff_id, salary, super_staff_id, canteen_id, aadhar)
        )
        print("Data inserted into STAFF table successfully")
    except Error as e:
        print(f"Error inserting into STAFF table: {e}")

# Function to insert data into the STAFF_DETAILS table
def insert_into_staff_details(cursor, aadhar, name, gender, dob):
    try:
        cursor.execute(
            "INSERT INTO STAFF_DETAILS (Aadhar, Name, Gender, DOB) VALUES (%s, %s, %s, %s)",
            (aadhar, name, gender, dob)
        )
        print("Data inserted into STAFF_DETAILS table successfully")
    except Error as e:
        print(f"Error inserting into STAFF_DETAILS table: {e}")

# Main function to take user input and perform the insertion
def main():
    # Establish a connection to the database
    connection = create_connection()

    if connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Get user input for STAFF table
        staff_id = int(input("Enter Staff ID: "))
        salary = int(input("Enter Salary: "))
        super_staff_id = int(input("Enter Super Staff ID (or enter 0 if none): "))
        canteen_id = input("Enter Canteen ID: ")
        aadhar = input("Enter Aadhar number: ")

        # Insert data into STAFF table
        insert_into_staff(cursor, staff_id, salary, super_staff_id, canteen_id, aadhar)

        # Get user input for STAFF_DETAILS table
        name = input("Enter Staff Name: ")
        gender = input("Enter Gender: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        # Insert data into STAFF_DETAILS table
        insert_into_staff_details(cursor, aadhar, name, gender, dob)

        # Commit changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
