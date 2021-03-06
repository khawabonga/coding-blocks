import sqlite3
from sqlite3 import Error
import os

HERE = os.path.dirname(__file__)

# ---------------------------------------------------
# Main

def main():
    dbPath = os.path.join(HERE, 'test_db.sqlite')
    tableName = 'test2'
    # Check if db exists
    dbExists = check_if_db_exists(dbPath)
    if dbExists:
        # Connect to db
        dbConn = create_connection(dbPath) # this creates the db if it doesn't exists
        # Check if table exists        
        tableExists = check_if_table_exists(dbConn, tableName)
        if tableExists:
            print('Table already exists!')
        else:
            # Create table
            query = (
                f'CREATE TABLE {tableName} (\n'
                'id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                'name TEXT NOT NULL,\n'
                'age INTEGER,\n'
                'gender TEXT,\n'
                'nationality TEXT\n'
                ');'
            )
            execute_query(dbConn, query)
# ---------------------------------------------------
# Methods

def execute_query(dbConnection, query):
    """
    Helper function to run queries with exception handling
    """
    print('---')
    print(f'dbConnection: {dbConnection}')
    print(f'Attempting to execute the following query: {query}')
    cursor = dbConnection.cursor()
    try:
        cursor.execute(query)
        dbConnection.commit()
        print('Query executed successfully!')
    except Error as e:
        print(f'An error occurred: {e}')
    #
    return cursor

def create_connection(dbFilePath):
    print('---')
    print(f'Connecting to database (file), dbFilePath={dbFilePath}')
    conn = None
    try:
        conn = sqlite3.connect(dbFilePath)
        print('Connection established')
    except Error as e:
        print(f'An error occurred: {e}')
    #
    print('--')
    return conn

def check_if_db_exists(dbFilePath):
    print('---')
    print(f'Checking if db exists at filepath={dbFilePath}')
    exists = False
    try:
        exists = os.path.isfile(dbFilePath)
        print(f'Success! db exists={exists}')
    except Exception as e:
        print(f'An exception occurred: {e}')
    #
    print('--')
    return exists


def check_if_table_exists(dbConn, tableName):
    print('---')
    print(f'Checking if a table with name={tableName} exists in db={dbConn}')
    exists = False
    try:
        cursor =dbConn.cursor()
        cursor.execute(f'SELECT count(*) FROM sqlite_master WHERE type="table" AND name="{tableName}";')
        a = cursor.fetchall()
        if a[0][0]:
            exists = True
        print(f'Success! table exists={exists}')
    except Error as e:
        print(f'An error occurred: {e}')
    #
    print('--')
    return exists
# ---------------------------------------------------
# Execute (only if called explicitely as main)

if __name__ == '__main__':
    main()