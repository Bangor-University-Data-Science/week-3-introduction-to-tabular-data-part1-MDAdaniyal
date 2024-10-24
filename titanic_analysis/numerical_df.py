def get_numerical_df(df, numerical_features):
    return df[df.select_dtypes(exclude=['object']).columns.to_list()]