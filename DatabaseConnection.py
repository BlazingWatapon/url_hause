import sqlite3

# Database name
databaseName = "testDB.db"

# Connect to database
connection = sqlite3.connect(databaseName)

# Cursor
cursor = connection.cursor()



