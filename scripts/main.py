from user_query import UserQueryProcessor
from graph_generation import ai_graph
from sql_generation import *
from db import *
import pandas as pd

query = "Which industries employ the most people?"
print("query:")
print(query)

print("\n====================================")
print("GETTING SCHEMA:")
database = os.getenv("DB_NAME")
schema = db(database).schema
print(schema)
print("\n====================================")
print("PROCESSING QUERY:")

uqp = UserQueryProcessor()
print(uqp.process_user_query(query))

print("\n====================================")
print("GENERATING SQL:")
sql, response = ask_db(chain, query)
print(response)

print("\n====================================")
print("GENERATING GRAPH:")
formated_data = {"query": query, "sql": sql, "response":response}
ai_graph(formated_data)
