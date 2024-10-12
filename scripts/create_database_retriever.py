from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from dotenv import load_dotenv
import os
import json

# Load the environment variables from the .env file
load_dotenv('openai_key.env')

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Optionally, set it as an environment variable if needed for further use
os.environ["OPENAI_API_KEY"] = api_key

# Uncomment the below to use LangSmith. Not required.
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

db = SQLDatabase.from_uri("mysql://root:@localhost:3306/report_generator_tests")
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


# Function to read JSON from a file
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Make sure the file is formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

q = "Is there any association between the type of vehicle used and delivery time"
response, result = ask_db(chain, q)

# Usage example
file_path = '../base/test.json'  # replace with your JSON file path
#anychart_schema = read_json_file(file_path)
anychart_schema = {
  "title": "anychart",
  "description": "anychart format",
  "type": "object",
  "properties": {
    "chart": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "Pie",
            "Bar",
            "Line",
            "Area",
            "Column",
            "Scatter",
            "Bubble",
            "Funnel",
            "Pyramid",
            "Radar",
            "Polar",
            "HeatMap",
            "TreeMap",
            "TagCloud",
            "Sunburst",
            "Sparkline",
            "Bullet",
            "Gantt",
            "Stock",
            "Waterfall",
            "CircularGauge"
            ]
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "x": {
                "type": "string"
              },
              "value": {
                "type": "number"
              },
              "fill": {
                "type": "string"
              }
            },
            "required": ["x", "value"]
          }
        },
        "container": {
          "type": "string"
        }
      },
      "required": ["type", "data", "container"]
    }
  },
  "required": ["chart"]
}

prompt = f"""
    You are a data generation expert. Use MySQL results to visualize the data 
    into a anychart diagram. Here is the following information to help create 
    that chart:
    User Query: {q}
    SQL Generated: {response}
    SQL Result: {result}
"""

structured_llm = llm.with_structured_output(anychart_schema)
res = structured_llm.invoke(prompt)

print(res)
