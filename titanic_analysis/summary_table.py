import pandas as pd
def create_summary_table(df):
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Has Missing Values?': df.isnull().any().values,
        'Number of Unique Values': df.nunique().values
    }
   
    summary_df = pd.DataFrame(summary_data)
    return summary_df