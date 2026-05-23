import pdfplumber
import pandas as pd
import streamlit as st
@st.cache_data
def extract_text_from_pdf(pdf_file):

    full_text = ""

    with pdfplumber.open(pdf_file) as pdf:

        MAX_PAGES = 20
        for page in pdf.pages[:MAX_PAGES]:
            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text