import os, sys
from typing import Type
from pandas import Series
from langchain_openai import ChatOpenAI

llm = None


def initialize_llm(api_key: str = "") -> None:
    global llm  # Indicate that we are modifying the global variable
    os.environ['OPENAI_API_KEY'] = api_key
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Function to summarize each transcript
def summarize_text(text: str) -> str:
    messages = [
        ("system", "You are a helpful assistant skilled in summarizing transcripts."),
        ("user", f"Summarize the following text in a few key points:\n\n{text}")
    ]
    return llm.invoke(messages).content


def summarize_many_texts(texts_series: Type[Series]) -> list:
    texts = texts_series.to_list()
    summaries = []
    total = len(texts)
    for i in range(total):
        summaries.append(summarize_text(texts[i]))
        sys.stdout.write("\r{}/{}".format(i + 1, total))
        sys.stdout.flush()
    return summaries


def analyze_changes(summaries: list, prompt: str = None) -> str:
    """
    Analyze changes in themes, tone, or topics over time from a list of summaries.

    Parameters:
    summaries (list): A list of summary strings, each representing a different point in time.
    prompt (str): An optional custom prompt to guide the analysis.

    Returns:
    str: A detailed analysis of how the summaries evolve over time.
    """
    combined_summaries = "\n\n".join(f"Summary {i+1}: {summary}" for i, summary in enumerate(summaries))
    if prompt is None:
        prompt = (
            "The following are summaries of transcripts over time. Analyze and describe how the topics, tone, or themes "
            "change across these summaries. Provide a general overview of the evolution."
        )
    messages = [
        ("system", "You are a skilled analyst for identifying changes in themes, tone, or topics over time."),
        ("user", f"{prompt}\n\n{combined_summaries}")
    ]

    return llm.invoke(messages).content

