from sentence_transformers import SentenceTransformer
from typing import Type
from pandas import DataFrame
import torch

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader



def categorize(df: Type[DataFrame], col: str, categories: list, result_col: str = "Category") -> Type[DataFrame]:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = df[col].to_list()
    text_embeddings = model.encode(texts, convert_to_tensor=True, show_progress_bar=True)
    category_embeddings = model.encode(categories, convert_to_tensor=True, show_progress_bar=True)

    cosine_scores = torch.mm(text_embeddings, category_embeddings.transpose(0, 1))

    assigned_category_indices = torch.argmax(cosine_scores, dim=1)
    df[result_col] = [categories[index] for index in assigned_category_indices]

    return df


def get_embeddings(fname: str, text_splitter: Type[CharacterTextSplitter] = None, embedding = None) -> list:
    loader = TextLoader(fname)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        separator=".", chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    emb = OpenAIEmbeddings()
    input_texts = [d.page_content for d in docs]

    input_embeddings = emb.embed_documents(input_texts)
    text_embeddings = list(zip(input_texts, input_embeddings))
    return text_embeddings, emb

