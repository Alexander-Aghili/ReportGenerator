from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from graph_examples import *
import matplotlib.pyplot as plt
import seaborn as sns
import re

def plot_dotplot(df, x_col, y_col, title, hue_col=None):
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=df, x=x_col, y=y_col, hue=hue_col, jitter=0.25, dodge=True)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    if hue_col:
        plt.legend(title=hue_col)
    plt.show()

def plot_histogram(df, column, title, bins=10):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=bins, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_barchart(df, x_col, y_col, title):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x=x_col, y=y_col, palette="viridis")
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

# Load the environment variables from the .env file
load_dotenv('openai_key.env')

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Optionally, set it as an environment variable if needed for further use
os.environ["OPENAI_API_KEY"] = api_key

gfuncs = {"dotplot":  plot_dotplot, "histogram":  plot_histogram, "barchart":  plot_barchart}

def ai_graph(data):
    query = data["query"]
    sql = data["sql"]
    df = data["response"]

    prompt = f"""
    ORIGIONAL QUESTION:\n
    {query}\n\n
    SQL CODE:\n
    {sql}\n\n
    SELECT THE CORRECT CHART AND PARAMETERS, FROM:
    dotplot: x, y, title
    histogram: x, title
    barchart: x,y, title
    \n\n

    return your answer in the format of:
        chart type: * parameters *

        ex. dotchart: x1,x2, "x1 effect on x2"
    Do not return any additional text.
    """

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    message = [
            ("system", "You are a data scientist who will determine the correct way to graph a set of data. You will be given the origional prompt and SQL code, determine what chart type to use"), 
            ("human", prompt)]
    ans = llm.invoke(message).content
    print(ans)

    gtype, temp = [i.strip() for i in ans.split(":")]
    fields = tuple( [i.strip().replace("\"", "") for i in temp.split(",")])
    print(fields)

    try:
        if gtype in gfuncs.keys():
            func = gfuncs[gtype]
            func(df, *fields )
    except Exception as e:
        print(f"AI Graph failed due to {e}")

if __name__ == "__main__":
    for ex in examples:
        ai_graph(ex)
