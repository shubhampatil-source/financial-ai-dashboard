import pdfplumber
import pandas as pd


def extract_tables_from_pdf(pdf_file):

    all_tables = []

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:

                if table:

                    df = pd.DataFrame(table)

                    all_tables.append(df)

    return all_tables