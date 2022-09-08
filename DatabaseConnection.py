import sqlite3

# Database name
databaseName = "C:/sqlite/testDB.db"

# Connect to database
connection = sqlite3.connect(databaseName)

# Cursor
cursor = connection.cursor()



