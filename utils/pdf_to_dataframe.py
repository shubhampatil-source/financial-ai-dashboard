import pandas as pd

def json_to_dataframe(financial_json):

    # IF DICTIONARY
    if isinstance(financial_json, dict):

        return pd.DataFrame([financial_json])

    # IF LIST
    elif isinstance(financial_json, list):

        return pd.DataFrame(financial_json)

    else:

        raise Exception(
            f"Invalid financial_json type: {type(financial_json)}"
        )