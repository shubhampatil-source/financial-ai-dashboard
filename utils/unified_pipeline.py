from utils.pdf_extractor import extract_text_from_pdf
from utils.ai_engine import extract_financial_metrics
from utils.pdf_to_dataframe import json_to_dataframe
from utils.table_extractor import extract_financial_tables
def process_financial_pdf(uploaded_file):

    # EXTRACT RAW TEXT
    pdf_text = extract_text_from_pdf(
        uploaded_file
    )

    # EXTRACT FINANCIAL TABLES
    tables = extract_financial_tables(
        uploaded_file
    )

    combined_tables = ""

    for table in tables:

        combined_tables += table.to_string()

    # SEND TABLES TO LLM
    financial_json = extract_financial_metrics(
        combined_tables
    )

    financial_df = json_to_dataframe(
        financial_json
    )

    return financial_df, pdf_text