import pandas as pd

def extract_data(file_path):
    """Extract data from CSV file."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Transform data: clean missing, duplicates, standardize."""
    # Drop columns with all missing values
    df = df.dropna(axis=1, how='all')
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Standardize text fields: strip whitespace
    text_columns = ['sector', 'track', 'jobrole', 'critical_work_function', 'task', 'task_type', 'task_category']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.strip()
    
    return df

def load_data(df, output_path):
    """Load data to CSV file."""
    df.to_csv(output_path, index=False)
    print(f'Data loaded to {output_path}')

def run_etl(input_path, output_path):
    """Run the full ETL pipeline."""
    df = extract_data(input_path)
    df_cleaned = transform_data(df)
    load_data(df_cleaned, output_path)
    print('ETL pipeline completed.')

if __name__ == '__main__':
    input_file = 's_users_jobrole_task.csv'
    output_file = 'cleaned_s_users_jobrole_task.csv'
    run_etl(input_file, output_file)