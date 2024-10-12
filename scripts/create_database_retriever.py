from langchain_community.utilities import SQLDatabase
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# Uncomment the below to use LangSmith. Not required.
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

db = SQLDatabase.from_uri("mysql://root:password@localhost:3306/report_generator_tests")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM deliveries LIMIT 10;")


