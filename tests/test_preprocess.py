from src.preprocess import load_and_clean_csv

def test_preprocessing():
    df = load_and_clean_csv("data/sample.csv")

    # dataframe should not be empty
    assert not df.empty

    # no missing values should remain
    assert df.isnull().sum().sum() == 0