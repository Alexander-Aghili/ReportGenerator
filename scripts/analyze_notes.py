import pandas as pd
from openai import OpenAI
import tiktoken


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('salesforce_accounts_notes.csv')

# Aggregate all notes into a single string
aggregated_notes = ' '.join(df['notes'].dropna()[:100].tolist()).replace("Remarks: ", "/")

# Optionally, print or inspect the aggregated notes
print(aggregated_notes)

def count_tokens(text, model="gpt-4"):
    # Get the encoding for the specified model
    encoding = tiktoken.encoding_for_model(model)
    # Encode the text to get the list of tokens
    tokens = encoding.encode(text)
    # Return the number of tokens
    return len(tokens)

# Define the function to summarize aggregated sentiment
def summarize_aggregated_sentiment(text):
    prompt = f"""
    Analyze the following aggregated customer notes and provide a concise summary of the general sentiment and key associations:
    """
    toks = count_tokens(prompt)
    toks += count_tokens(text)
    if toks > 3000:
        print(toks)
        print("stopping")
        return


    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
            ],
        max_tokens=1000,
        temperature=0.1,
    )
    print(response.usage.total_tokens)
    summary = response.choices[0].message.content.strip()
    return summary

# Summarize the general sentiment
general_sentiment_summary = summarize_aggregated_sentiment(aggregated_notes)

print("General Sentiment Summary:")
print(general_sentiment_summary)
