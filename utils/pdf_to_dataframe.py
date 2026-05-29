import pandas as pd


def json_to_dataframe(financial_json):

    if isinstance(financial_json, dict):

        df = pd.DataFrame([financial_json])

    elif isinstance(financial_json, list):

        df = pd.DataFrame(financial_json)

    else:

        raise Exception(
            f"Invalid format: {type(financial_json)}"
        )

    # ----------------------------
    # CLEAN COLUMN NAMES
    # ----------------------------

    df.columns = [
        str(col).strip().replace(" ", "_")
        for col in df.columns
    ]

    # ----------------------------
    # CLEAN NUMERIC VALUES
    # ----------------------------

    for col in df.columns:

        if col != "Year":

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("₹", "")
                .str.strip()
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # YEAR CLEANUP

    if "Year" in df.columns:

        df["Year"] = pd.to_numeric(
            df["Year"],
            errors="coerce"
        )

    return df