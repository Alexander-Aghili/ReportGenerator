import nltk
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset
from nltk.tokenize import sent_tokenize
from scipy.special import softmax
import numpy as np
import os

# Download NLTK data files (only need to run once)
# nltk.download('punkt')

# Check if GPU is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Load FinBERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
model = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone')

model.to(device)

def analyze_sentiment(text, batch_size=32):
    """
    Analyzes the overall sentiment of the provided text.

    Args:
        text (str): The unstructured text to analyze.
        batch_size (int): The number of sentences to process in a batch.

    Returns:
        float: The overall sentiment score ranging from -1 (negative) to +1 (positive).
    """
    # Split text into sentences
    sentences = sent_tokenize(text)

    # Encode all sentences
    inputs = tokenizer(
        sentences,
        add_special_tokens=True,
        max_length=512,
        truncation=True,
        padding=True,
        return_tensors='pt'
    )

    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Create a DataLoader for batching
    dataset = TensorDataset(input_ids, attention_mask)
    #dataloader = DataLoader(dataset, batch_size=batch_size)
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        pin_memory=True  # Useful if you're using GPUs
        )

    sentiment_scores = []

    # Process batches
    for batch in dataloader:
        batch_input_ids = batch[0].to(device)
        batch_attention_mask = batch[1].to(device)

        with torch.no_grad():
            outputs = model(input_ids=batch_input_ids, attention_mask=batch_attention_mask)
            logits = outputs.logits.cpu().numpy()
            probabilities = softmax(logits, axis=1)

            # Calculate sentiment scores for the batch
            batch_scores = probabilities[:, 2] - probabilities[:, 0]
            sentiment_scores.extend(batch_scores)

    # Calculate the average sentiment score
    if sentiment_scores:
        overall_score = np.mean(sentiment_scores)
    else:
        overall_score = 0.0

    # Normalize the score to be between -1 and +1
    overall_score = max(min(overall_score, 1.0), -1.0)

    print(overall_score)
    return overall_score

if __name__ == '__main__':
    pass
