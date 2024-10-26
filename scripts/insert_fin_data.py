#!/bin/python3

import pandas as pd
import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np

# Assuming `df` is your DataFrame

# Database connection setup
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',    # Update with your host
            user='root',    # Update with your MySQL username
            password='', # Update with your MySQL password
            database='financial_data'  # Update with your database name
        )
        if connection.is_connected():
            print("Connection successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to dynamically generate and execute the insert query
def insert_data(connection, data, db):
    cursor = connection.cursor()

    # Get column names dynamically from the DataFrame
    columns = data.columns
    columns_str = ', '.join("`" + columns + "`")
    placeholders = ', '.join(['%s'] * len(columns))
    insert_query = f"INSERT INTO {db.upper()} ({columns_str}) VALUES ({placeholders})"
  
    data = data.replace({np.nan: None})
    i = 0
    for row in data.itertuples(index=False, name=None):
        i += 1
        try:
            print(i) 
            cursor.execute(insert_query, row)
        except Error as e:
            print(f"Failed to insert data: {e}")
            connection.rollback()  # Rollback if there's an error in inserting

    connection.commit()
    cursor.close()

def main():
    db = 'sub'
    # Load data from the TSV file
    tsv_file_path = '../datasets/2024_q3/' + db + '.tsv'  # Update with the path to your TSV file
    data = pd.read_csv(tsv_file_path, delimiter='\t')

    # Create database connection and insert data
    connection = create_connection()
    if connection:
        insert_data(connection, data, db)
        connection.close()

if __name__ == "__main__":
    main()

