import mysql.connector
import os
import re
from sqlalchemy import create_engine

user = os.environ.get("DB_USER")
pw = os.environ.get("DB_PASSWORD")

class db:
    def __init__(self, db_name):
        # Database connection parameters
        self.config = {
            'user': user,
            'password': pw,
            'host': 'localhost',
            'database': db_name,
       }

        try:
            # Create an Engine
            self.engine = create_engine("mysql+mysqlconnector://", creator=self.get_connection)

            # Establish the connection
            self.connection = self.get_connection()
            self.cursor = self.connection.cursor()

            # Get a list of the tables
            self.cursor.execute("SHOW TABLES;")
            self.tables = [f[0] for f in self.cursor.fetchall()]

            tables_schema = []
            # Find schema for each table
            for table in self.tables:
                # Find schema for a table
                self.cursor.execute(f"SHOW CREATE TABLE {table};")

                # Strip the returned string into a nice list
                text = self.cursor.fetchall()[0][1]
                pattern = r'\(\n(.*?)\n\)'
                schema_temp = re.findall(pattern, text, re.DOTALL)[0]
                columns = schema_temp.split(",\n")
                
                schema = []
                for col in columns:
                    if "KEY" not in col:
                        pattern = r'`(.*?)`'
                        name = re.findall(pattern, col, re.DOTALL)[0]
                        details = (col.split(f"`{name}`")[-1].strip())
                        schema.append((name,details))

                tables_schema.append( (table, dict(schema)))

            self.schema = dict(tables_schema)
        


        except Exception as e:
            print(f"Cannot connect to {db_name} \nReason:")
            print(e)
            return None
    
    def get_connection(self):
        return mysql.connector.connect(**self.config)

    # A function to safely close the connection to the database
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if self.engine:
            self.engine.dispose()
