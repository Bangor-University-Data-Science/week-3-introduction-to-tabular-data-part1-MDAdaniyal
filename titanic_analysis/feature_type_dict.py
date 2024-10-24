import pandas as pd
def create_feature_type_dict(titanic_df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }
    
    numerical_columns = titanic_df.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_columns:
        if titanic_df[col].dtype == 'int64':  
            feature_types['numerical']['discrete'].append(col)
        else:  
            feature_types['numerical']['continuous'].append(col)
    
    categorical_columns = titanic_df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_columns:
        if col in ['Pclass']: 
            feature_types['categorical']['ordinal'].append(col)
        else:
            feature_types['categorical']['nominal'].append(col)
    
    return feature_types
