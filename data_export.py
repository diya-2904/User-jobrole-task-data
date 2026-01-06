import pandas as pd
import json

def export_csv(df, output_path):
    """Export DataFrame to CSV."""
    df.to_csv(output_path, index=False)
    print(f'Data exported to CSV: {output_path}')

def export_json(df, output_path):
    """Export DataFrame to JSON."""
    df.to_json(output_path, orient='records')
    print(f'Data exported to JSON: {output_path}')

def run_data_exports(input_path, csv_output, json_output):
    """Load data and export to CSV and JSON."""
    df = pd.read_csv(input_path)
    export_csv(df, csv_output)
    export_json(df, json_output)

if __name__ == '__main__':
    input_file = 'cleaned_s_users_jobrole_task.csv'
    csv_snapshot = 'data_snapshot.csv'
    json_snapshot = 'data_snapshot.json'
    run_data_exports(input_file, csv_snapshot, json_snapshot) 