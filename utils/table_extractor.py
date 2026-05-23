import pdfplumber
import pandas as pd

def extract_financial_tables(pdf_file):

    tables_data = []

    with pdfplumber.open(pdf_file) as pdf:

        for page_num, page in enumerate(pdf.pages):

            text = page.extract_text()

            if text:

                # DETECT FINANCIAL PAGES
                keywords = [
                    "balance sheet",
                    "statement of profit",
                    "assets",
                    "liabilities",
                    "revenue",
                    "net profit"
                ]

                if any(
                    keyword.lower() in text.lower()
                    for keyword in keywords
                ):

                    tables = page.extract_tables()

                    for table in tables:

                        if table:

                            df = pd.DataFrame(table)

                            tables_data.append(df)

    return tables_data