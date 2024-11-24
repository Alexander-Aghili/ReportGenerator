import pickle
import sys
import os
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import pandas as pd

# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from src import analysis_a

# Replace 'file_path.pkl' with the path to your .pkl file
file_path = '../tests/data/motley-fool-data.pkl'

# Open the file in binary read mode
with open(file_path, 'rb') as file:
    data = pickle.load(file)


# Extract the texts from the 5th column (index 4)
texts = data.iloc[:, 4]
multiprocessing.set_start_method('spawn', force=True)

if __name__ == '__main__':

    sentiments = []

    for i in range(0, len(texts)):
        score = analysis_a.analyze_sentiment(texts[i])
        print(score)
        print("Completed " + str(i) + "/" + str(len(texts)))
        sentiments.append(score)

    data['sentiment'] = sentiments
    print(data)

    # Write data to a CSV file
    data.to_csv('output.csv', index=False)

