import pandas as pd
def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    feat_list = df.select_dtypes(include=['object']).columns.to_list()
    feature_unique_values = {}
    for ft in feat_list:
        feature_unique_values[ft] = df[ft].unique()
    return feature_unique_values