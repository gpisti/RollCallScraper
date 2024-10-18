import pandas as pd

def save_data_to_csv(merged_df, file_path):
    """Save the merged dataframe to a CSV file."""
    merged_df.to_csv(file_path, index=False)
