# Multimodal RAG Application Using Qdrant and Gemini for Healthcare Applications
![Python](https://img.shields.io/badge/python-3.9-blue)
![LLM](https://img.shields.io/badge/LLM-Enabled-orange)
![Gemini](https://img.shields.io/badge/Gemini-Google-red)
![Vector DB](https://img.shields.io/badge/Vector%20DB-Qdrant-grey)
![Qdrant](https://img.shields.io/badge/Qdrant-Search%20Engine-green)

Project Overview
---
This project builds a Retrieval-Augmented Generation (RAG) system combining Google's Gemini, Qdrant, and a custom application for efficient query and response handling.

#Pipeline Workflow
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
Query input
Query retrieval
Response delivery

#Key Technologies
Google Gemini: Image and document summarization
Qdrant: Vector database for indexing and searching
Guardio: Application layer for query-response management
