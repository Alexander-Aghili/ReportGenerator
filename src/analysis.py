from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Type
from pandas import DataFrame, Series
import sys

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def analyze_sentiment(text: str) -> int:
    # Tokenize the review
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=None)
    outputs = model(**inputs)
    logits = outputs.logits
    # Apply softmax to get probabilities
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    
    negative_score = probabilities[0][0].item()
    positive_score = probabilities[0][1].item()
    
    # Compute sentiment score on a scale of -1 to 1
    sentiment_score = positive_score - negative_score

    return sentiment_score


def analyze_sentiment_series(series: Type[Series], progress: bool = False) -> list[int]:
    texts_list = series.to_list()
    scores = []
    total = len(texts_list)

    for i in range(total):
        item = texts_list[i]
        score = analyze_sentiment(item)
        scores.append(score)
        if progress:
            sys.stdout.write("\r{}/{}".format(i + 1, total))
            sys.stdout.flush()
    return scores


def analyze_sentiment_dataframe_add_column(df: Type[DataFrame], col: str, col_name: str ="sentiment", progress: bool = False) -> Type[DataFrame]:
    scores = analyze_sentiment_series(df[col], progress=progress)
    df[col_name] = scores
    return df 
