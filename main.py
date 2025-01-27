import  mysql.connector
from mysql.connector import Error

#import create_database_query.py
import create_database_query as cdq

#import create_data_table_queries.py
import create_data_table_queries as cdtq

#import populate_data_tables_queries.py
import populate_data_tables_queries as pdtq

import delete_queries as dq

import update_queries as uq
import read_data_tables_queries as rdtq
def createServerConnection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name

        )
        print("MySQL Database Connection Successful!!")

    except Error as err:
        print(f"Error:{err}")
    return  connection
#create a function that will create a database
def create_database(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully!!")
    except Error as err:
        print(f"Error: {err}")

#create work horse function to execute queries
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful!!")
    except Error as err:
        print(f"Error: '{err}'")


#create a function to read information from data tables from Data Base
def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#call function to establish connection from main.py to mySQL
connection = createServerConnection("localhost","root","student","school")

#display information form data tables in pycharm


execute_query(connection,dq.delete_course)
print("Information for Course Table: ")
courseDataTable = read_query(connection, rdtq.display_course_table_information)
for courseInformation in courseDataTable:
    print(courseInformation)
print()