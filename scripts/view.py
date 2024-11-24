import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('output.csv')

# Ensure the 'sentiment' column is of float type
df['sentiment'] = df['sentiment'].astype(float)

# Create sentiment bins from 0 to 0.2 with 0.01 intervals
bins = np.arange(0, 0.31, 0.01)  # 0.21 to include 0.2 in the bins
labels = [round(b, 2) for b in bins[:-1]]  # Labels for x-axis

# Bin the sentiment scores
df['sentiment_bin'] = pd.cut(
    df['sentiment'],
    bins=bins,
    labels=labels,
    include_lowest=True,
    right=False
)

# Filter out any sentiments outside the range [0, 0.2]
df = df.dropna(subset=['sentiment_bin'])

# Count the number of rows in each sentiment bucket
counts = df['sentiment_bin'].value_counts().sort_index()

# Plot the column chart
plt.figure(figsize=(15, 7))
counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.xlabel('Sentiment Bins (0.01 intervals from 0 to 0.2)')
plt.ylabel('Number of Rows')
plt.title('Number of Rows in Each Sentiment Bucket')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

