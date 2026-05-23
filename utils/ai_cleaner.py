import ollama
import json
from groq import Groq
import streamlit as st
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
def clean_financial_schema(raw_metrics):

    prompt = f"""
    You are a financial data validation system.

    Clean and validate this financial data.

    Rules:
    - Ensure numeric consistency
    - Fill missing fields if inferable
    - Keep schema standardized
    - Return ONLY valid JSON

    Data:
    {raw_metrics}
    """

    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}])
    answer = response.choices[0].message.content
    return answer