from textblob import TextBlob
from typing import Type
from pandas import DataFrame, Series
import sys


def analyze_sentiment(text: str) -> int:
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    return score


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
