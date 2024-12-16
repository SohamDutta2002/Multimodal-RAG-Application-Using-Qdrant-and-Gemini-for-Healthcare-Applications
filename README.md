# Multimodal RAG Application Using Qdrant and Gemini for Healthcare Applications
![Python](https://img.shields.io/badge/python-3.9-blue)
![LLM](https://img.shields.io/badge/LLM-Enabled-orange)
![Gemini](https://img.shields.io/badge/Gemini-Google-red)
![Vector DB](https://img.shields.io/badge/Vector%20DB-Qdrant-grey)
![Qdrant](https://img.shields.io/badge/Qdrant-Search%20Engine-green)

Project Overview
---
This project builds a Retrieval-Augmented Generation (RAG) system combining Google's Gemini, Qdrant, and a custom application for efficient query and response handling.

Pipeline Workflow
---
*Input: Image + DoctorNotes

*Images and notes are fed into the pipeline for processing.
Gemini Integration

Google Gemini processes the input to perform:
Image summarization
Document notes extraction
Data extraction
Outputs are parsed using a Pydantic class.
Node Parser

Extracted and summarized data is structured into nodes for indexing.
Qdrant (Vector Database)

The parsed data is stored as vectors in Qdrant for efficient retrieval.
Index Creation: Organizes the vectorized data for queries.
Query Engine & Retrieval

The Query Engine processes user queries and retrieves relevant information using Qdrant.
The system provides responses based on retrieved data.
App (Guardio)

The application integrates the entire pipeline and facilitates:
- Query input
- Query retrieval
- Response delivery

Key Technologies
---
- Google Gemini: Image and document summarization
- Qdrant: Vector database for indexing and searching
- Guardio: Application layer for query-response management

Setting Up the Environment
---
Install Required Libraries <br>
```
!pip install llama-index
!pip install 'google-generativeai>=0.3.0' qdrant_client
!pip install llama-index-multi-modal-llms-gemini
!pip install llama-index-vector-stores-qdrant
!pip install llama-index-embeddings-gemini
!python3 -m pip install --upgrade qdrant-client fastembed Pillow
!pip install llama-index-llms-gemini
!pip install pyarrow==15.0.2
!pip uninstall -y pyarrow datasets
!pip install datasets sentence_transformers
!pip install llama-index-embeddings-clip
!pip install git+https://github.com/openai/CLIP.git
!pip install llama-index-embeddings-fastembed
!pip install --upgrade langchain-experimental qdrant-client datasets sentence_transformers

!pip install gradio
!pip install pyngrok
```
Download and Preprocess the ROCO Dataset<br>
```
!git clone https://github.com/razorx89/roco-dataset.git
cd roco-dataset
!python /content/roco-dataset/scripts/fetch.py -d
```

