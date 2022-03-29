import pandas as pd

def get_dataframe(json_path):
    return pd.read_json(json_path, lines=True)

def get_top_10_retweets(dataframe):
    _dataframe = dataframe.copy()
    
    return _dataframe.sort_values('retweetCount', ascending=False)['retweetCount'].head(10)

