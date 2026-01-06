import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_distributions(df):
    print("Data Distributions:")
    categorical_cols = [
        'sector', 'track', 'jobrole',
        'critical_work_function',
        'task_type', 'task_category'
    ]
    for col in categorical_cols:
        if col in df.columns:
            print(f"\n{col} value counts:")
            print(df[col].value_counts())

# Cramér's V function
def cramers_v_safe(contingency):
    chi2, _, _, _ = chi2_contingency(contingency)
    n = contingency.sum().sum()
    r, c = contingency.shape

    # Avoid division by zero
    if min(r, c) <= 1:
        return np.nan

    return np.sqrt(chi2 / (n * (min(r, c) - 1)))

def calculate_correlations(df):
    print("\nCorrelation Analysis (Cramer's V for categorical variables):")

    # Sector vs Track
    if 'sector' in df.columns and 'track' in df.columns:
        contingency = pd.crosstab(df['sector'], df['track'])
        cramer_v = cramers_v_safe(contingency)

        if np.isnan(cramer_v):
            print("Cramer's V between sector and track: Not applicable")
        else:
            print(f"Cramer's V between sector and track: {cramer_v:.3f}")

def identify_patterns(df):
    print("\nPattern Identification:")

    # Job roles per track
    print("Job roles per track:")
    print(df.groupby('track')['jobrole'].nunique())

    # Tasks per jobrole
    print("\nTasks per jobrole:")
    print(df.groupby('jobrole')['task'].count().head(5))

def run_eda(input_path):
    df = load_data(input_path)
    analyze_distributions(df)
    calculate_correlations(df)
    identify_patterns(df)

if __name__ == '__main__':
    input_file = 'cleaned_s_users_jobrole_task.csv'
    run_eda(input_file)