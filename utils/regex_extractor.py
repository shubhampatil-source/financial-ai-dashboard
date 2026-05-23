import re


def extract_financial_metrics(text):

    patterns = {

        "Revenue":
        r"Revenue[:\s]+\$?([\d,]+)",

        "Expenses":
        r"Expenses[:\s]+\$?([\d,]+)",

        "Net_Profit":
        r"Net Profit[:\s]+\$?([\d,]+)",

        "Assets":
        r"Assets[:\s]+\$?([\d,]+)",

        "Liabilities":
        r"Liabilities[:\s]+\$?([\d,]+)"
    }

    extracted = {}

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            value = match.group(1)

            value = value.replace(",", "")

            extracted[key] = float(value)

        else:

            extracted[key] = None

    return extracted