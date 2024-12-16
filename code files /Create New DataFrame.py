import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from fastembed import TextEmbedding, ImageEmbedding
from qdrant_client import QdrantClient, models
from PIL import Image

# Load the CSV file into a DataFrame
df = pd.read_csv("/content/data.csv")

# List all image files in the specified directory
images = os.listdir('/content/roco-dataset/data/test/radiology/images')

# Filter the DataFrame to include only rows with images that exist in the directory
new_df_data = []
for i in df['Image']:
    if i + '.jpg' in images:
        row = df[df['Image'] == i]
        new_df_data.append([i, row['DoctorNote'].values[0]])

# Create a new DataFrame with the filtered data
new_df = pd.DataFrame(new_df_data, columns=['Image', 'DoctorNote'])[:5]
print(new_df)
