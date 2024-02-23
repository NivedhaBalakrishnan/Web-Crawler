from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import configparser



config = configparser.ConfigParser()
config.read('config.ini')

# Load the DataFrame from the CSV file
file_name = config.get('DATABASE', 'output_file')
url_df = pd.read_csv(file_name)
url_titles = url_df['Title'].tolist()

# Load the Embedding Model
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

# Encode the URL titles
emb = model.encode(url_titles)

emb_str = [','.join(map(str, e)) for e in emb]

# Save it to Embedding column in the DataFrame
url_df['Embedding'] = [list(e) for e in emb]

# # Save the DataFrame to a CSV file
url_df.to_csv(file_name, index=False)

