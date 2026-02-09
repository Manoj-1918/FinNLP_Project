import pandas as pd
import re

def clean_data():
    df = pd.read_csv("data/raw_headlines.csv")

    def clean_text(text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
        return text

    df["headline"] = df["headline"].apply(clean_text)
    df.to_csv("data/processed_headlines.csv", index=False)
    return df
