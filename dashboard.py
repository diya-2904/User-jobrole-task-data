import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Job Role Task Dashboard')

# Load data
df = pd.read_csv('cleaned_s_users_jobrole_task.csv')

st.header('Current Data Status')
st.write('Overview of cleaned dataset:')
st.dataframe(df.head())

st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", len(df))
col2.metric("Total Job Roles", df['jobrole'].nunique())
col3.metric("Total Sectors", df['sector'].nunique())
col4.metric("Total Tracks", df['track'].nunique())


st.subheader('Job Roles per Track')
track_jobrole = df.groupby('track')['jobrole'].nunique()
st.bar_chart(track_jobrole)

st.subheader('Task Types Distribution')
task_type_dist = df['task_type'].value_counts()
st.bar_chart(task_type_dist)

st.subheader('Tasks per Job Role')
jobrole_tasks = df.groupby('jobrole')['task'].count().sort_values(ascending=False)
st.bar_chart(jobrole_tasks.head(10))

st.header('Mock ML Predictions')
# Mock predictions for demonstration
unique_roles = df['jobrole'].unique()
predictions = np.random.choice(unique_roles, size=len(df))
df['predicted_jobrole'] = predictions

st.subheader('Prediction Sample')
sample_df = df[['jobrole', 'predicted_jobrole']].sample(10)
st.dataframe(sample_df)

st.subheader('Mock Accuracy')
accuracy = (df['jobrole'] == df['predicted_jobrole']).mean()
st.metric('Accuracy', f'{accuracy:.2%}')

st.write('Note: Predictions are mocked. Actual ML models will replace this.')