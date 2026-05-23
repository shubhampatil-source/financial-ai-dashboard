from groq import Groq
import streamlit as st
import json
import re

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_financial_insights(kpis):
    prompt = f"""You are a senior financial analyst. Analyze these KPIs: {kpis}
    Provide:
    - Key insights
    - Risks
    - Recommendations
    """
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def financial_chat(question, financial_context):
    prompt = f"""You are an AI financial analyst. Use the financial data below to answer the user question.
    Financial Context:{financial_context}
    User Question:{question}
    Answer professionally and clearly.
    """
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def analyze_pdf_report(pdf_text):
    prompt = f"""You are a senior financial analyst. Analyze this financial report.
    Identify:
    - Key financial trends
    - Risks
    - Growth indicators
    - Business concerns
    Report:{pdf_text[:4000]}
    """
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def rag_financial_chat(question,relevant_chunks):
    context = "\n".join(relevant_chunks)
    prompt = f"""You are a financial AI assistant. Use ONLY the provided context to answer the question.
    Context:{context}
    Question:{question}
    Provide a professional financial answer."""
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def executive_summary(financial_context):
    prompt = f"""Create an executive-level financial summary.
    Include:
    - business performance
    - profitability
    - financial risks
    - strategic recommendations
    Context:{financial_context}"""
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def detect_financial_risks(kpis):
    prompt = f"""Analyze these KPIs for financial risks. KPIs: {kpis}
    Identify:
    - liquidity risks
    - profitability concerns
    - debt concerns
    - operational risks"""
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def ai_company_comparison(comparison_data):
    prompt = f"""Compare the financial performance of two companies.
    Data:{comparison_data}
    Provide:
    - stronger company
    - profitability comparison
    - risk comparison
    - strategic observations"""
    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer

def extract_financial_metrics(pdf_text):

    # -----------------------------------
    # VALIDATE PDF TEXT
    # -----------------------------------

    if not pdf_text or pdf_text.strip() == "":

        raise Exception(
            "PDF text extraction failed."
        )

    # LIMIT TEXT SIZE
    pdf_text = pdf_text[:4000]

    prompt = f"""
    Extract the financial values from this report.

    Return ONLY valid JSON.

    NO explanations.
    NO markdown.
    NO ```json.

    REQUIRED FORMAT:

    {{
        "Revenue": 0,
        "Expenses": 0,
        "Net_Profit": 0,
        "Assets": 0,
        "Liabilities": 0
    }}

    Financial Report:
    {pdf_text}
    """

    # -----------------------------------
    # GROQ CALL
    # -----------------------------------

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    # -----------------------------------
    # RAW RESPONSE
    # -----------------------------------

    result = response.choices[0].message.content

    # DEBUG
    print("\n========== RAW LLM RESPONSE ==========\n")
    print(result)

    # -----------------------------------
    # EMPTY RESPONSE CHECK
    # -----------------------------------

    if result is None:

        raise Exception(
            "LLM returned None response."
        )

    result = result.strip()

    if result == "":

        raise Exception(
            "LLM returned empty response."
        )

    # -----------------------------------
    # REMOVE MARKDOWN
    # -----------------------------------

    result = re.sub(r"```json", "", result)
    result = re.sub(r"```", "", result)

    result = result.strip()

    # -----------------------------------
    # EXTRACT JSON SAFELY
    # -----------------------------------

    json_match = re.search(r"\{.*\}", result, re.DOTALL)

    if not json_match:

        raise Exception(
            f"No JSON found in response:\n\n{result}"
        )

    json_string = json_match.group()

    print("\n========== CLEAN JSON ==========\n")
    print(json_string)

    # -----------------------------------
    # PARSE JSON
    # -----------------------------------

    try:

        financial_json = json.loads(json_string)

        return financial_json

    except Exception as e:

        raise Exception(
            f"""
JSON Parsing Failed

ERROR:
{e}

RAW RESPONSE:
{result}
"""
        )