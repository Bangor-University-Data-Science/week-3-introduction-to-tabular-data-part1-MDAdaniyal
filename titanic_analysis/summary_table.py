import pandas as pd
def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    titanic_df = pd.read_csv('titanic.csv')

    summary = pd.DataFrame({
    'Feature Name': titanic_df.columns,
    'Data Type': titanic_df.dtypes.values,
    'Number of Unique Values': titanic_df.nunique().values,
    'Has Missing Values?': titanic_df.isnull().any().values
     })
    return summary
