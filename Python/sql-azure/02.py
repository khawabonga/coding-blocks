import pyodbc
import os 
from dotenv import load_dotenv

here = os.path.dirname(__file__)
envFile = os.path.join(here, '.env')
load_dotenv(envFile)

DRIVER = os.getenv('ODBC_DRIVER')
SERVER = os.getenv('SERVER_NAME')
PORT = 1433
DATABASE = os.getenv('DATABASE_NAME')
UID = os.getenv('USER_NAME')
PWD = os.getenv('USER_PASSWORD')

configString = ''
configString += 'DRIVER={};'.format(DRIVER)
configString += 'SERVER={};'.format(SERVER)
configString += 'PORT={};'.format(PORT)
configString += 'DATABASE={};'.format(DATABASE)
configString += 'UID={};'.format(UID)
configString += 'PWD={}'.format(PWD)

with pyodbc.connect(configString) as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            '''
            CREATE TABLE Person
            (
                PersonId INT IDENTITY PRIMARY KEY,
                FirstName NVARCHAR(128) NOT NULL,
                MiddelInitial NVARCHAR(10),
                LastName NVARCHAR(128) NOT NULL,
                DateOfBirth DATE NOT NULL
            )
            '''
        )
        