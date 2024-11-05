from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv('openai_key.env')

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Optionally, set it as an environment variable if needed for further use
os.environ["OPENAI_API_KEY"] = api_key

# Uncomment the below to use LangSmith. Not required.
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

db = SQLDatabase.from_uri("mysql://root:@localhost:3306/sales_data")
llm = ChatOpenAI(model="gpt-4o-mini")
chain = create_sql_query_chain(llm, db)

def ask_db(chain, question):
    response = chain.invoke({"question": question})
    response = response.replace("SQLQuery: ", "")
    response = response.replace("sql", "")
    response = response.replace("```", "")
    print(response)
    result = db.run(response)
    print(result)
    return response, result


question = "What is the quarterly sales of our largest customer?"
ask_db(chain, question)
