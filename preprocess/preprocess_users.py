import pandas as pd
import os

# Define the relative paths for the source and destination folders
source_file = '../data/etl_results/flattened_survey_data.csv'
destination_folder = '../data/star_tables'
# Load the CSV file into a DataFrame
df = pd.read_csv(source_file)

# Filter the DataFrame for DEMOGRAPHICS type and required subtypes
demographics_df = df[(df['type'] == 'DEMOGRAPHICS') & (df['subtype'].isin(['AGE', 'GENDER', 'PHONE', 'RACE']))]

# Create individual DataFrames for each subtype
age_df = demographics_df[demographics_df['subtype'] == 'AGE'][['user_id', 'numeric_answer']].rename(columns={'numeric_answer': 'age'})
gender_df = demographics_df[demographics_df['subtype'] == 'GENDER'][['user_id', 'selected_answer_id']].rename(columns={'selected_answer_id': 'gender'})
phone_df = demographics_df[demographics_df['subtype'] == 'PHONE'][['user_id', 'free_text']].rename(columns={'free_text': 'phone'})
race_df = demographics_df[demographics_df['subtype'] == 'RACE'][['user_id', 'selected_answer_id']].rename(columns={'selected_answer_id': 'race'})

# Use outer joins to ensure all users are included
dim_users = age_df.merge(gender_df, on='user_id', how='outer')
dim_users = dim_users.merge(phone_df, on='user_id', how='outer')
dim_users = dim_users.merge(race_df, on='user_id', how='outer')

# Ensure all expected columns are present
expected_columns = ['user_id', 'age', 'gender', 'phone', 'race']
for col in expected_columns:
    if col not in dim_users.columns:
        dim_users[col] = pd.NA

# Reorder columns to match the expected order
dim_users = dim_users[expected_columns]

# Remove duplicate rows if any
dim_users = dim_users.drop_duplicates()

# Save the DimUsers dataframe to a CSV file
output_path = destination_folder + '/DimUsers.csv'
dim_users.to_csv(output_path, index=False)

print(f"DimUsers dataframe has been saved to {output_path}")