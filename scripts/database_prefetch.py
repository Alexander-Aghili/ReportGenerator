import mysql.connector
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv('db.env')

# Establish a database connection
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# Get list of tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Loop through each table and fetch structure and data
for (table_name,) in tables:
    print(f"\nTable: {table_name}")

    # Get table structure
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    print("Structure:")
    for column in columns:
        print(column)

    # Fetch data (limit to 5 rows)
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
    rows = cursor.fetchall()
    print("Example Data:")
    for row in rows:
        print(row)

# Close the connection
cursor.close()
conn.close()

