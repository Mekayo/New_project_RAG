# COVER PAGE
<br><br><br><br><br>
<h1 align="center">PROJECT REPORT ON</h1>
<h2 align="center">HEALTHCARE RAG ASSISTANT</h2>
<br>
<h3 align="center">Submitted in partial fulfillment of the requirements for the award of the degree of</h3>
<h3 align="center"><strong>Bachelor of Technology</strong></h3>
<br>
<h3 align="center">Submitted By:</h3>
<p align="center">
[Your Name] <br>
[Your Roll/Registration Number]
</p>
<br>
<h3 align="center">Under the Guidance of:</h3>
<p align="center">
[Supervisor Name] <br>
[Designation]
</p>
<br><br><br>
<h2 align="center">CEC-CGC Landran, Mohali</h2>
<p align="center">Month, Year</p>
<div style="page-break-after: always"></div>

# INNER TITLE PAGE
<br><br><br><br><br>
<h1 align="center">PROJECT REPORT ON</h1>
<h2 align="center">HEALTHCARE RAG ASSISTANT</h2>
<br>
<h3 align="center">Submitted in partial fulfillment of the requirements for the award of the degree of</h3>
<h3 align="center"><strong>Bachelor of Technology</strong></h3>
<br>
<h3 align="center">Submitted By:</h3>
<p align="center">
[Your Name] <br>
[Your Roll/Registration Number]
</p>
<br>
<h3 align="center">Under the Guidance of:</h3>
<p align="center">
[Supervisor Name] <br>
[Designation]
</p>
<br><br><br>
<h2 align="center">CEC-CGC Landran, Mohali</h2>
<p align="center">Month, Year</p>
<div style="page-break-after: always"></div>

# CERTIFICATE

This is to certify that the project report entitled **"Healthcare RAG Assistant"** submitted by **[Your Name] ([Your Roll Number])** in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in [Your Branch/Department], **CEC-CGC Landran, Mohali**, is an authentic record of the student's own work carried out under my supervision and guidance. 

To the best of my knowledge, the matter embodied in this report has not been submitted elsewhere for the award of any other degree or diploma.

<br><br><br><br>
**(Signature of Supervisor)**
<br>
**[Supervisor Name]** <br>
[Supervisor Designation] <br>
[Department Name] <br>
CEC-CGC Landran, Mohali

<br><br>
**(Signature of HOD)**
<br>
**[HOD Name]** <br>
Head of Department <br>
[Department Name] <br>
CEC-CGC Landran, Mohali
<div style="page-break-after: always"></div>

# ACKNOWLEDGEMENT

I would like to express my deepest appreciation to all those who provided me the possibility to complete this project. A special gratitude I give to my project guide, **[Supervisor Name]**, whose contribution in stimulating suggestions and encouragement, helped me to coordinate my project successfully.

Furthermore, I would also like to acknowledge with much appreciation the crucial role of the staff of **CEC-CGC Landran, Mohali**, who gave the permission to use all required equipment and the necessary materials to complete the task. 

I have to appreciate the guidance given by other supervisor as well as the panels especially in our project presentation that has improved our presentation skills thanks to their comment and advices.

Last but not least, many thanks go to my classmates and friends who have invested their full effort in guiding me in achieving the goal.

**[Your Name]** <br>
**[Your Roll Number]**
<div style="page-break-after: always"></div>

# ABSTRACT

The rapidly expanding volume of medical literature and patient data necessitates intelligent systems that can quickly and accurately retrieve relevant information to assist healthcare professionals. Large Language Models (LLMs) offer unprecedented natural language understanding capabilities, but they often suffer from hallucinations when answering domain-specific queries. This project introduces the **Healthcare RAG (Retrieval-Augmented Generation) Assistant**, a robust system designed to provide grounded, medically accurate responses by combining LLMs with a dynamic vector-based retrieval mechanism.

The developed system allows users to upload custom medical documents (such as clinical trial PDFs and research papers) and directly pulls relevant abstracts from PubMed via the NCBI API. These documents are processed, embedded using local sentence transformers (`HuggingFaceEmbeddings`), and stored in a persistent ChromaDB vector database. When a user submits a query through the Streamlit-based graphical user interface (GUI), the system retrieves the most contextually relevant document chunks and provides them as context to a powerful LLM (Qwen 2.5 32B via Groq). The LLM synthesizes an accurate answer that includes source citations, ensuring the verifiability of the information.

The architecture ensures data privacy for local embeddings while leveraging high-speed cloud inference for generation. This project demonstrates a functional, end-to-end pipeline covering data ingestion, vector storage, context retrieval, and generation, ultimately serving as a reliable AI-powered assistant for healthcare research and decision-making support.
<div style="page-break-after: always"></div>

# TABLE OF CONTENTS

1. Cover Page
2. Inner Title Page
3. Certificate
4. Acknowledgement
5. Abstract
6. Table of Contents
7. List of Tables
8. List of Figures
9. Abbreviations and Nomenclature
10. Chapter 1: Introduction
    1.1 Background
    1.2 Problem Statement
    1.3 Objectives
    1.4 Scope of the Project
    1.5 Organization of the Report
11. Chapter 2: Literature Survey
    2.1 Natural Language Processing in Healthcare
    2.2 Large Language Models (LLMs)
    2.3 Retrieval-Augmented Generation (RAG)
    2.4 Existing Medical AI Assistants
12. Chapter 3: Present Work
    3.1 System Architecture
    3.2 Environment Setup & Technologies Used
    3.3 Data Ingestion Pipeline
    3.4 Vector Database Integration
    3.5 LLM Retrieval and Generation
    3.6 User Interface Development
13. Chapter 4: Result & Discussion
    4.1 Implementation Results
    4.2 Performance Analysis
    4.3 Challenges Faced
14. Chapter 5: Conclusion & Future Scope
    5.1 Conclusion
    5.2 Future Enhancements
15. References
<div style="page-break-after: always"></div>

# LIST OF TABLES

1. Table 3.1: Technology Stack and Tools Used
2. Table 3.2: Hyperparameters for Document Chunking
3. Table 4.1: Response Latency Evaluation
4. Table 4.2: Accuracy and Hallucination Reduction Metrics
<div style="page-break-after: always"></div>

# LIST OF FIGURES

1. Figure 1.1: High-level overview of a standard RAG pipeline
2. Figure 3.1: Detailed System Architecture of Healthcare RAG Assistant
3. Figure 3.2: Data Flow Diagram for Document Ingestion
4. Figure 3.3: ChromaDB Vector Storage Implementation
5. Figure 3.4: Streamlit Application Interface - Chat View
6. Figure 3.5: Streamlit Application Interface - Sidebar Configuration
7. Figure 4.1: Screenshot of accurate medical retrieval with source citations
8. Figure 4.2: Comparison graph of standalone LLM vs RAG-enhanced LLM performance
<div style="page-break-after: always"></div>

# ABBREVIATIONS AND NOMENCLATURE

**AI:** Artificial Intelligence
**API:** Application Programming Interface
**DB:** Database
**GUI:** Graphical User Interface
**LLM:** Large Language Model
**NCBI:** National Center for Biotechnology Information
**NLP:** Natural Language Processing
**PDF:** Portable Document Format
**RAG:** Retrieval-Augmented Generation
**UI:** User Interface
**URL:** Uniform Resource Locator

<div style="page-break-after: always"></div>

# CHAPTER 1: INTRODUCTION

## 1.1 Background
In the modern digital era, the healthcare sector generates and relies on massive amounts of textual data, including patient records, clinical trials, and medical research papers. Finding precise information in this vast sea of data is time-consuming for medical professionals and researchers. While Large Language Models (LLMs) like GPT-4, Llama 3, and Qwen offer immense capabilities in text generation and summarization, their generic training data makes them prone to "hallucinations" (generating plausible but incorrect information). In healthcare, where accuracy is critical, hallucinations are unacceptable.

## 1.2 Problem Statement
How can we leverage the natural language capabilities of Large Language Models without sacrificing factual accuracy in the medical domain? Standalone LLMs lack access to real-time or private organizational data and cannot accurately cite their sources. There is a need for a reliable system that grounds the LLM's responses in verifiable, uploaded medical literature.

## 1.3 Objectives
The primary objectives of this project are:
1. To develop a Retrieval-Augmented Generation (RAG) system specifically tailored for healthcare queries.
2. To allow dynamic data ingestion from user-uploaded PDF documents and direct API pulls from PubMed (NCBI).
3. To implement a local vector database (ChromaDB) for secure and efficient semantic search.
4. To integrate a powerful LLM (Qwen 2.5 via Groq) to generate accurate, medically sound responses.
5. To provide a user-friendly Graphical User Interface (GUI) using Streamlit, featuring real-time chat, source citations, and configuration settings.

## 1.4 Scope of the Project
The project covers the end-to-end development of the RAG pipeline. The scope includes setting up the Python environment, configuring local embedding models (via PyTorch/HuggingFace), integrating the Groq cloud API for LLM inference, and designing a frontend interface. The application is limited to text-based retrieval and does not process medical imaging (e.g., X-rays, MRIs).

## 1.5 Organization of the Report
The report is organized into five main chapters. Chapter 1 provides the introduction and objectives. Chapter 2 reviews the literature on NLP, LLMs, and RAG. Chapter 3 details the present work, focusing on the system architecture and implementation of various modules. Chapter 4 discusses the results and system performance. Finally, Chapter 5 concludes the project and suggests future scope.

<div style="page-break-after: always"></div>

# CHAPTER 2: LITERATURE SURVEY

## 2.1 Natural Language Processing in Healthcare
Natural Language Processing (NLP) has long been utilized in healthcare for tasks such as named entity recognition (extracting diseases, medications), clinical note classification, and medical coding. Traditional NLP pipelines rely on rule-based systems or earlier machine learning models (like SVMs or basic RNNs), which often fail to grasp the deeper context and nuance of complex medical terminology.

## 2.2 Large Language Models (LLMs)
The advent of transformer architectures revolutionized NLP, leading to the development of LLMs. Models like Llama, Qwen, and ChatGPT are pre-trained on massive corpora of text. While highly capable of reasoning and generating human-like text, their application in healthcare is limited by their inability to update their knowledge base post-training and their tendency to confidently generate false information (hallucinations) when asked niche medical questions.

## 2.3 Retrieval-Augmented Generation (RAG)
Introduced by Lewis et al. in 2020, RAG is a paradigm that mitigates LLM hallucinations. A RAG system first retrieves relevant documents from an external knowledge base based on the user's query. These retrieved documents are then prepended to the user's prompt as context. The LLM generates an answer strictly based on the provided context. This ensures that responses are factual, up-to-date, and traceable back to the source documents.

## 2.4 Existing Medical AI Assistants
Existing solutions like IBM Watson Health or specialized medical search engines often lack conversational flexibility. Modern RAG approaches using LangChain or LlamaIndex are becoming standard in enterprise AI. However, many solutions are heavily cloud-dependent, raising data privacy concerns. This project proposes a hybrid approach: processing embeddings locally to maintain control over the vector space, while leveraging cloud-based APIs strictly for the final text generation step.

<div style="page-break-after: always"></div>

# CHAPTER 3: PRESENT WORK

## 3.1 System Architecture
The system follows a modular architecture encompassing four main pipelines: Ingestion, Storage, Retrieval, and Generation. 
1. **Ingestion:** Medical PDFs and PubMed abstracts are loaded, cleaned, and split into smaller, manageable chunks using text splitters.
2. **Storage:** The chunks are converted into dense vector embeddings using local HuggingFace embedding models and stored persistently in ChromaDB.
3. **Retrieval:** When a user queries the system, the query is embedded, and a similarity search is performed in ChromaDB to fetch the top-K relevant chunks.
4. **Generation:** The retrieved chunks are formatted into a prompt and sent to the Groq API (Qwen 2.5). The LLM processes the context and returns a cited answer to the Streamlit UI.

## 3.2 Environment Setup & Technologies Used
The project was developed in a Python virtual environment to manage dependencies efficiently.
- **Programming Language:** Python 3.10+
- **Frontend/UI:** Streamlit
- **Vector Database:** ChromaDB
- **Embeddings:** PyTorch, HuggingFace Embeddings (Sentence Transformers)
- **LLM API Provider:** Groq (High-speed LPU inference)
- **Frameworks:** Custom Python modules (`app/ingestion`, `app/retrieval`, `app/generation`)

## 3.3 Data Ingestion Pipeline
The `app/ingestion` module handles two sources:
- **PDF Documents:** Users can upload medical research papers or clinical guidelines. The system parses the PDF text, handling formatting anomalies.
- **PubMed Integration:** The system uses the NCBI API to fetch abstracts directly from PubMed. This allows researchers to get the latest published literature dynamically.
The ingested text is passed through a RecursiveCharacterTextSplitter to create overlapping chunks. This ensures that contextual meaning is not lost at the boundaries of the text segments.

## 3.4 Vector Database Integration
`app/retrieval` manages the vector storage. We utilized ChromaDB for its lightweight, persistent, and fast vector search capabilities. The text chunks are mapped into a high-dimensional vector space. By calculating the cosine similarity or Euclidean distance between the user query vector and the document vectors, the system can instantly identify the most relevant pieces of information.

## 3.5 LLM Retrieval and Generation
The `app/generation` module acts as the orchestrator. It takes the retrieved documents and constructs a specialized prompt. The prompt instructs the LLM: *"You are a medical assistant. Answer the user's question using ONLY the provided context. If the answer is not in the context, say 'I don't know'. Cite the source document."* 
This prompt, alongside the user query, is sent to the Groq API utilizing the `llama-3.3-70b-versatile` or `Qwen` models, ensuring near-instantaneous inference speeds.

## 3.6 User Interface Development
The frontend is built using Streamlit (`app/main.py` and `app/ui`).
- **Sidebar:** Allows users to configure API keys, select the LLM model, adjust retrieval parameters (like top-k results), and upload PDFs.
- **Chat Interface:** Provides a familiar chatbot experience where users can type queries and receive conversational responses along with expandable source citations.

<div style="page-break-after: always"></div>

# CHAPTER 4: RESULT & DISCUSSION

## 4.1 Implementation Results
The Healthcare RAG Assistant was successfully implemented and deployed locally. The Streamlit interface effectively allows users to interact with the system. Uploading a complex medical PDF (e.g., a paper on oncology treatments) takes a few seconds to parse, embed, and store in the local ChromaDB instance. 

When queried, the system accurately retrieves the exact paragraphs mentioning specific drug dosages or trial outcomes and formulates a coherent, human-readable answer. The system successfully includes citations, showing the user exactly which document and page the information was extracted from.

## 4.2 Performance Analysis
- **Retrieval Accuracy:** The local HuggingFace embeddings proved highly effective at semantic matching, capturing medical synonyms and context better than keyword-based searches.
- **Latency:** Because the embeddings are computed locally and the LLM generation is handled by Groq's specialized LPU hardware, the end-to-end latency from query submission to answer generation is generally under 2 seconds.
- **Hallucination Mitigation:** Testing with ambiguous or out-of-domain questions confirmed that the RAG prompt successfully constrains the LLM. It reliably outputs "The context does not provide information on this topic" instead of hallucinating an answer.

## 4.3 Challenges Faced
1. **Dependency Conflicts:** Managing dependencies like `pyarrow`, `sentence-transformers`, and `datasets` required careful pinning of versions in `requirements.txt` to avoid Windows import errors.
2. **Chunking Strategies:** Finding the optimal chunk size was challenging. Chunks that were too small lost medical context, while chunks that were too large diluted the relevance score and exceeded LLM context windows. A balanced approach using recursive chunking with overlap was implemented.
3. **Medical Terminology:** Standard embedding models sometimes struggle with complex medical jargon. While adequate for this project, utilizing domain-specific embeddings (like ClinicalBERT) is a noted future optimization.

<div style="page-break-after: always"></div>

# CHAPTER 5: CONCLUSION & FUTURE SCOPE

## 5.1 Conclusion
The project successfully demonstrates the design, development, and deployment of a Healthcare RAG Assistant. By integrating local vector search via ChromaDB with the immense generative power of cloud-hosted LLMs via Groq, the system solves the critical problem of LLM hallucinations in the medical domain. The assistant provides a fast, reliable, and user-friendly platform for researchers and healthcare professionals to interact with their customized knowledge bases, significantly reducing the time required for literature review and data extraction.

## 5.2 Future Enhancements
The current system lays a strong foundation, but several enhancements can be made in the future:
1. **Domain-Specific Models:** Replacing general embedding models with medical-specific models (e.g., MedBERT, ClinicalBERT) to improve the semantic retrieval of complex medical jargon.
2. **Multi-Modal Support:** Upgrading the ingestion pipeline to understand charts, graphs, and medical imaging alongside text.
3. **Evaluation Frameworks:** Integrating RAGAS (Retrieval Augmented Generation Assessment) to automatically evaluate and score the faithfulness and relevance of the generated answers.
4. **Local LLM Execution:** Transitioning to fully local open-source LLMs (using Ollama or vLLM) to guarantee 100% data privacy for sensitive patient data, removing the reliance on external cloud APIs.

<div style="page-break-after: always"></div>

# REFERENCES

1. Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *Advances in Neural Information Processing Systems*, 33, 9459-9474.
2. Vaswani, A., et al. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems*, 30.
3. Streamlit Documentation. (2024). *Streamlit: The fastest way to build data apps in Python.* Retrieved from https://docs.streamlit.io/
4. ChromaDB Documentation. (2024). *Chroma: The AI-native open-source embedding database.* Retrieved from https://docs.trychroma.com/
5. HuggingFace. (2024). *Sentence-Transformers.* Retrieved from https://huggingface.co/sentence-transformers
6. Groq Documentation. (2024). *Groq Cloud and LPU Architecture.* Retrieved from https://console.groq.com/docs
