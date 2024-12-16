# Prepare documents for embedding
documents = []
for index, row in new_df.iterrows():
    documents.append({
        "caption": row['DoctorNote'],
        "image": f'/content/roco-dataset/data/test/radiology/images/{row["Image"]}.jpg'
    })

print(documents)

# Load the CLIP model for image and text embeddings
model = SentenceTransformer('clip-ViT-B-32')
client = QdrantClient(":memory:")
