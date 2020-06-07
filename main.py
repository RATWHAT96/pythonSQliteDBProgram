import sqlite3


# Class defining operation on the database
class DBOperations:
    # Fields containing SQLite expressions
    sql_create_table = "CREATE TABLE 'EmployeeUoB' (employeeID INTEGER(20),title VARCHAR(5),forename VARCHAR(20),surname CHAR(1),email VARCHAR(20),salary INTEGER UNSIGNED, PRIMARY KEY (employeeID))"
    sql_insert = "INSERT INTO EmployeeUoB (employeeID,title,forename,surname,email,salary) VALUES(?,?,?,?,?,?)"
    sql_select_all = "SELECT * FROM EmployeeUoB ORDER BY employeeID"
    sql_search = "SELECT * from EmployeeUoB where employeeID = ?"
    sql_update_data = "UPDATE EmployeeUoB SET Title = ?, Forename = ?, Surname = ?, Email = ?, Salary = ?  WHERE EmployeeID = ?"
    sql_delete_data = "DELETE FROM EmployeeUoB WHERE EmployeeID = ?"

    # Creates database file
    def get_connection(self):
        self.conn = sqlite3.connect("EmployeeRACR20.db")
        self.cur = self.conn.cursor()

    # Creates new table
    def create_table(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_create_table)
            self.conn.commit()
            print("Table created successfully")
        except Exception:
            print("Warning: EmployeeUoB already exists")
        finally:
            self.conn.close()

    # Inserts data into new table
    def insert_data(self):
        try:
            self.get_connection()
            emp = Employee()
            emp.set_employee_id(int(input("Enter Employee ID: ")))
            emp.set_employee_title(str(input("Enter Employee Title: ")))
            emp.set_forename(str(input("Enter Employee Forename: ")))
            emp.set_surname(str(input("Enter Employee Surname: ")))
            emp.set_email(str(input("Enter Employee Email: ")))
            emp.set_salary(int(input("Enter Employee Salary: ")))

            self.cur.execute(self.sql_insert, tuple(str(emp).split("\n")))
            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # Displays all dat in table
    def select_all(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all)
            results = self.cur.fetchall()
            for row in results:
                print("EmployeeID: ", row[0])
                print("Title: ", row[1])
                print("Forename: ", row[2])
                print("Surname: ", row[3])
                print("Email: ", row[4])
                print("Salary: ", row[5])
                print("\n")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # Find Employee data using Employee ID
    def search_data(self):
        try:
            self.get_connection()
            employeeID = int(input("Enter Employee ID: "))
            self.cur.execute(self.sql_search, tuple(str(employeeID).split('\n')))
            result = self.cur.fetchone()
            if type(result) == type(tuple()):
                for index, detail in enumerate(result):
                    if index == 0:
                        print("Employee ID: " + str(detail))
                    elif index == 1:
                        print("Employee Title: " + detail)
                    elif index == 2:
                        print("Employee Name: " + detail)
                    elif index == 3:
                        print("Employee Surname: " + detail)
                    elif index == 4:
                        print("Employee Email: " + detail)
                    else:
                        print("Salary: " + str(detail))
            else:
                print("No Record")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # Edit existing data
    def update_data(self):
        try:
            self.get_connection()

            # Update statement
            emp = Employee()
            emp.set_employee_title(str(input("Enter Employee Title: ")))
            emp.set_forename(str(input("Enter Employee Forename: ")))
            emp.set_surname(str(input("Enter Employee Surname: ")))
            emp.set_email(str(input("Enter Employee Email: ")))
            emp.set_salary(int(input("Enter Employee Salary: ")))
            emp.set_employee_id(int(input("Enter Employee ID: ")))

            list1 = list(str(emp).split('\n'))
            employeeID = list1[0]
            list1 = list1[1:]
            list1.append(employeeID)
            result = self.cur.execute(self.sql_update_data, tuple(list1))
            print(tuple(list1))

            self.conn.commit()
            if result.rowcount != 0:
                print(str(result.rowcount) + "Row(s) affected.")
            else:
                print("Record can not find in the database")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # Delete existing data
    def delete_data(self):
        try:
            self.get_connection()
            employeeID = int(input("Enter Employee ID: "))
            result = self.cur.execute(self.sql_delete_data, tuple(str(employeeID).split('\n')))
            self.conn.commit()
            if result.rowcount != 0:
                print(str(result.rowcount) + "Row(s) affected.")
            else:
                print("Record can not find in the database")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


# Employee object class containing set and get methods for employee data fields
class Employee:
    def __init__(self):
        self.employeeID = 0
        self.empTitle = ''
        self.forename = ''
        self.surname = ''
        self.email = ''
        self.salary = 0.0

    def set_employee_id(self, employeeID):
        self.employeeID = employeeID

    def set_employee_title(self, empTitle):
        self.empTitle = empTitle

    def set_forename(self, forename):
        self.forename = forename

    def set_surname(self, surname):
        self.surname = surname

    def set_email(self, email):
        self.email = email

    def set_salary(self, salary):
        self.salary = salary

    def get_employee_id(self):
        return self.employeeId

    def get_employee_title(self):
        return self.empTitle

    def get_forename(self):
        return self.forename

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_salary(self):
        return self.salary

    def __str__(self):
        return str(
            self.employeeID) + "\n" + self.empTitle + "\n" + self.forename + "\n" + self.surname + "\n" + self.email + "\n" + str(
            self.salary)

# Program loop with commands to manage employee database
while True:
    print("\n Menu:")
    print("**********")
    print(" 1. Create table EmployeeUoB")
    print(" 2. Insert data into EmployeeUoB")
    print(" 3. Select all data into EmployeeUoB")
    print(" 4. Search an employee")
    print(" 5. Update data some records")
    print(" 6. Delete data some records")
    print(" 7. Exit\n")

    __choose_menu = int(input("Enter your choice: "))
    db_ops = DBOperations()
    if __choose_menu == 1:
        db_ops.create_table()
    elif __choose_menu == 2:
        db_ops.insert_data()
    elif __choose_menu == 3:
        db_ops.select_all()
    elif __choose_menu == 4:
        db_ops.search_data()
    elif __choose_menu == 5:
        db_ops.update_data()
    elif __choose_menu == 6:
        db_ops.delete_data()
    elif __choose_menu == 7:
        print("Program exited")
        break
    else:
        print("Invalid Choice")
