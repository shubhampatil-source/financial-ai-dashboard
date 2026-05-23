required_columns = [
    "Revenue",
    "Expenses",
    "Net_Profit",
    "Assets",
    "Liabilities"
]


def validate_schema(data):

    validated = {}

    for column in required_columns:

        validated[column] = data.get(column)

    return validated