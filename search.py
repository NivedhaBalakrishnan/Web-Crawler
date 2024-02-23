from sentence_transformers import SentenceTransformer
import pandas as pd
import configparser
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys


config = configparser.ConfigParser()
config.read('config.ini')

# read csv
url_df = pd.read_csv(config.get('DATABASE', 'output_file'))


# Load the Embedding Model
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

# Function to convert space-separated string representation of embedding to numpy array
def parse_embedding(embedding_str):
    values = embedding_str.strip('[]').split(',')
    values = [val for val in values if val.strip()]
    return np.array([float(val) for val in values])

url_df['Embedding'] = url_df['Embedding'].apply(parse_embedding)


def find_similar_urls(query, url_df):
    # Get the embedding vector for the query string
    query_embedding = model.encode(query)
    
    # Calculate cosine similarity between the query embedding and all embeddings in url_df
    similarities = url_df['Embedding'].apply(lambda x: cosine_similarity([query_embedding], [x])[0][0])
    
    # Sort URLs by similarity in descending order and get top 5
    top_urls_indices = similarities.argsort()[::-1][:5]
    top_urls = url_df.iloc[top_urls_indices]
    
    return top_urls


# Test the function
query = ' '.join(sys.argv[1:])
top_urls = find_similar_urls(query, url_df)

# Print the Title and URL for each row in top_urls
for index, row in top_urls[['URL', 'Title']].iterrows():
    print(f"Title: {row['Title']}, URL: {row['URL']}")
