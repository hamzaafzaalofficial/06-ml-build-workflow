import pandas as pd

def load_and_clean_csv(path: str):
    df = pd.read_csv(path)
    df = df.dropna()
    return df