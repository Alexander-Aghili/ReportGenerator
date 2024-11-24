from sentence_transformers import SentenceTransformer
from typing import Type
from pandas import DataFrame
import torch


def categorize(df: Type[DataFrame], col: str, categories: list, result_col: str = "Category") -> Type[DataFrame]:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = df[col].to_list()
    text_embeddings = model.encode(texts, convert_to_tensor=True, show_progress_bar=True)
    category_embeddings = model.encode(categories, convert_to_tensor=True, show_progress_bar=True)

    cosine_scores = torch.mm(text_embeddings, category_embeddings.transpose(0, 1))

    assigned_category_indices = torch.argmax(cosine_scores, dim=1)
    df[result_col] = [categories[index] for index in assigned_category_indices]

    return df


