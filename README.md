# AI Financial Intelligence Dashboard

An end-to-end **AI-powered financial analysis dashboard** built with **Streamlit, Python, and Generative AI** to automate financial report processing.

The application converts unstructured PDF financial reports into structured financial data, calculates key KPIs, generates AI-powered insights, and enables context-aware Q&A through Retrieval-Augmented Generation (RAG).

---

## Project Objective

Financial reports often contain large amounts of unstructured information that take time to analyze manually.

The objective of this project is to simplify and automate this workflow by:

- Extracting financial text directly from PDF reports
- Identifying key financial metrics using LLMs
- Transforming extracted data into structured DataFrames
- Calculating KPIs and financial ratios automatically
- Generating AI-powered financial insights
- Allowing users to ask document-specific questions using RAG
- Displaying results through an interactive dashboard

---

## Features

### Financial Report Upload
- Upload financial statements in PDF format
- Supports direct document analysis from Streamlit UI

### Automated Text Extraction
- Extracts raw text from PDF using:
  - **PyMuPDF**
  - **pdfplumber**

### AI Financial Data Extraction
- Uses **Groq LLM (Llama 3.1)** to:
  - Extract financial metrics
  - Convert text into structured JSON
  - Generate contextual insights

### Data Cleaning & Parsing
- Converts JSON output into:
  - Pandas DataFrames
  - Standardized tabular format

### KPI & Ratio Calculation
Examples:
- Revenue Growth
- Profit Margin
- Operating Margin
- EBITDA
- Liquidity Metrics

### Retrieval-Augmented Generation (RAG)
- Stores extracted document text in **FAISS Vector DB**
- Retrieves relevant chunks
- Answers user queries based on report context

### Dashboard & Visualizations
- Interactive KPI cards
- Charts & graphs using Plotly
- AI-generated insights
- Q&A section

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyMuPDF, pdfplumber |
| AI/LLM | Groq (Llama 3.1) |
| Data Processing | Pandas |
| Vector Database | FAISS |
| Visualization | Plotly |

---

## Project Workflow

### 1. Upload PDF
User uploads a financial report.

### 2. Text Extraction
Raw text extracted from PDF.

### 3. AI Extraction
LLM extracts structured financial metrics.

### 4. Parsing & Cleaning
JSON converted to DataFrame.

### 5. KPI Calculation
Financial KPIs and ratios calculated.

### 6. AI Insights + RAG
Generate insights and answer questions.

### 7. Dashboard Output
Display:
- Structured Data
- KPI metrics
- Charts
- Insights
- Q&A

---


## Future Improvements

- Multi-company comparison
- Historical trend analysis
- Export insights to PDF/Excel
- Advanced financial benchmarking
- Forecasting using ML

---

## Key Learnings

This project helped strengthen:

- Generative AI integration in analytics
- Retrieval-Augmented Generation (RAG)
- Financial KPI automation
- Streamlit deployment
- Building end-to-end AI analytics applications

---

## Author

**Shubham Patil**  
Data Analytics | SQL | Power BI | Python | Generative AI
