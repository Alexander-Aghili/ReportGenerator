import mysql.connector

# Establish a database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alexWa0720",
    database="sales_data"
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

