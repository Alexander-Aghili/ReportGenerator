import pandas as pd
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
import mysql.connector
import time
import include_openai
import lotus
from lotus.models import LM, LiteLLMRM
from sentence_transformers import SentenceTransformer, util


lotus.settings.configure(
    lm=lotus.models.LM(
        api_key=os.environ["OPENAI_API_KEY"],
        model="gpt-4o-mini",
    ),
    rm = lotus.models.LiteLLMRM(model="text-embedding-3-small")
)

# Load environment variables from .env file
load_dotenv('db.env')

# Read environment variables
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")

connstring = f"mysql://{user}:{password}@{host}:{port}/{database}"

config = {
    'user': user,
    'password': password,
    'host': host,
    'database': database,
}


def get_connection():
    return mysql.connector.connect(**config)


db_engine = create_engine("mysql+mysqlconnector://", creator=get_connection)


def execute_db(query):
    result = pd.read_sql(query, db_engine)
    return result


accounts_df = execute_db("SELECT * FROM accounts;")
contacts_df = execute_db("SELECT * FROM contacts;")
opportunities_df = execute_db("SELECT * FROM opportunities;")


# Helper function to clean and convert currency fields to float
def parse_currency(value):
    try:
        return float(value.replace('$', '').replace(',', ''))
    except Exception:
        return 0.0

plt.ion()

# Prepare Accounts table for revenue analysis
accounts_df['revenue'] = accounts_df['revenue'].apply(parse_currency)


def aggregate_category(df, list_aggregate, list_given, category_name):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    aggregate_embeddings = model.encode(list_aggregate, convert_to_tensor=True)

    given_embeddings = model.encode(list_given.tolist(), convert_to_tensor=True)

    aggregations = []
    for i, given_embedding in enumerate(given_embeddings):
        # Compute similarity with each major industry
        similarities = util.pytorch_cos_sim(given_embedding, aggregate_embeddings)
    # Find the index of the most similar major industry
        closest_major_industry_idx = similarities.argmax()
        aggregations.append(major_industries[closest_major_industry_idx])

    df[category_name] = aggregations

    return df

# Define your major industries
major_industries = [
    "Finance & Banking",
    "Healthcare & Pharmaceuticals",
    "Technology & Telecommunications",
    "Energy & Utilities",
    "Manufacturing & Industrial",
    "Consumer Goods & Retail",
    "Real Estate & Construction",
    "Media & Entertainment",
    "None"
    ]


aggregate_category(accounts_df, major_industries, accounts_df["industry"], "major_industry")

# Visualization 1: Revenue Distribution by Industry (Accounts Table)
revenue_by_industry = accounts_df.groupby('major_industry')['revenue'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
revenue_by_industry.plot(kind='bar')
plt.title("Average Revenue by Industry")
plt.xlabel("Industry")
plt.ylabel("Average Revenue ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show(block=False)

# Visualization 2: Employee Count by Region (Accounts Table)
employee_count_by_region = accounts_df.groupby('region')['employee_count'].sum().sort_values(ascending=False)
# Separate the top 5 regions and aggregate the rest into "Other"
top_5 = employee_count_by_region[:5]
other = pd.Series([employee_count_by_region[5:].sum()], index=["Other"])

# Concatenate the top 5 and "Other" into a single Series
employee_count_top5_other = pd.concat([top_5, other])

# Plot the bar chart
plt.figure(figsize=(10, 6))
employee_count_top5_other.plot(kind='bar')
plt.title("Total Employee Count by Region (Top 5 + Other)")
plt.xlabel("Region")
plt.ylabel("Total Employee Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show(block=False)

# Visualization 3: Account Type Distribution (Accounts Table)
account_type_counts = accounts_df['account_type'].value_counts()
plt.figure(figsize=(8, 8))
account_type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Account Type Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show(block=False)

categories = [
    "Healthcare and Wellness",
    "Engineering and Technical Roles",
    "Administrative and Support",
    "Sales and Marketing",
    "Information Technology",
    "Finance and Accounting",
    "Education and Research",
    "Human Resources and Recruitment"
]

print(aggregate_category(contacts_df, categories, contacts_df["title"], "overall_title"))
# Visualization 4: Contact Titles Distribution (Contacts Table)
title_distribution = contacts_df['overall_title'].value_counts().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
title_distribution.plot(kind='bar')
plt.title("Contact Titles Distribution")
plt.xlabel("Title")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show(block=False)

input()
