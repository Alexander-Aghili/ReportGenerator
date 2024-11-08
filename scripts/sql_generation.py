from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from dotenv import load_dotenv
import mysql.connector
import os
import pandas as pd
from sqlalchemy import create_engine

# Load the environment variables from the .env file
load_dotenv('openai_key.env')

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Optionally, set it as an environment variable if needed for further use
os.environ["OPENAI_API_KEY"] = api_key

# Uncomment the below to use LangSmith. Not required.
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Load environment variables from .env file
load_dotenv('db.env')

# Read environment variables
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")

connstring=f"mysql://{user}:{password}@{host}:{port}/{database}"
db = SQLDatabase.from_uri(connstring)
llm = ChatOpenAI(model="gpt-4o-mini")
chain = create_sql_query_chain(llm, db)

config = {
    'user': user,
    'password': password,
    'host': host,
    'database': database,
}

def get_connection():
    return mysql.connector.connect(**config)

db_engine = create_engine("mysql+mysqlconnector://", creator=get_connection)

def ask_db(chain, question):
    response = chain.invoke({"question": question})
    response = response.replace("SQLQuery: ", "")
    response = response.replace("sql", "")
    response = response.replace("```", "")
    result = pd.read_sql(response, db_engine)
    print(result)
    return response, result


if __name__ == "__main__":
    question = "What is the quarterly sales of our largest customer?"
    ask_db(chain, question)
