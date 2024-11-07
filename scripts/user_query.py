# user_query.py

import re, sys
import nltk
from nltk.corpus import stopwords
from typing import List, Tuple

# Download NLTK stopwords if not already present
nltk.download("stopwords")


class UserQueryProcessor:
    def __init__(self):
        self.padding_words = set(stopwords.words("english"))  # Common words to remove
        self.sql_keywords = ["SELECT", "FROM", "WHERE", "JOIN", "ORDER BY", "GROUP BY", "LIMIT"]

    def clean_user_query(self, query: str) -> str:
        """
        Cleans the user query by converting to lowercase, removing padding words,
        and stripping unnecessary punctuation.
        """
        # Convert to lowercase
        query = query.lower()

        # Remove punctuation
        query = re.sub(r'[^\w\s]', '', query)

        # Split the query into words and filter out padding words
        words = query.split()
        cleaned_query = " ".join(word for word in words if word not in self.padding_words)

        return cleaned_query

    def identify_keywords(self, cleaned_query: str) -> List[str]:
        """
        Identifies potential keywords from the cleaned query that may be
        useful for SQL generation.
        """
        # Split the cleaned query into words
        words = cleaned_query.split()

        # Filter out words that might be SQL-specific or indicate database fields
        keywords = [word for word in words if word.upper() in self.sql_keywords or len(word) > 3]

        return keywords

    def standardize_query_format(self, cleaned_query: str, keywords: List[str]) -> dict:
        """
        Standardizes the query into a structured dictionary format to facilitate
        SQL generation and further LLM processing.
        """
        standardized_format = {
            "original_query": cleaned_query,
            "keywords": keywords,
            "query_intent": "Generate SQL for data visualization"
        }

        return standardized_format

    def process_user_query(self, query: str) -> Tuple[str, List[str], dict]:
        """
        Main function to process the user's natural language query:
        - Cleans the query
        - Identifies keywords
        - Standardizes the query format
        """
        # Step 1: Clean the query
        cleaned_query = self.clean_user_query(query)

        # Step 2: Identify keywords for SQL query development
        keywords = self.identify_keywords(cleaned_query)

        # Step 3: Standardize the query format for SQL generation
        standardized_query = self.standardize_query_format(cleaned_query, keywords)

        return cleaned_query, keywords, standardized_query


# Example usage:
if __name__ == "__main__":
    processor = UserQueryProcessor()

    # Example user query
    user_query = sys.argv[1] if len(sys.argv) > 1 else "What was the quarterly EBITDA for the Meta Corporation and compare it against all other Big Tech companies"

    cleaned_query, keywords, standardized_query = processor.process_user_query(user_query)

    print("Cleaned Query:", cleaned_query)
    print("Keywords:", keywords)
    print("Standardized Query Format:", standardized_query)
