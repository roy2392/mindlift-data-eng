import pandas as pd

source_file = '../data/etl_results/flattened_survey_data.csv'
destination_folder = '../data/star_tables'
# Load the CSV file into a DataFrame
df = pd.read_csv(source_file)

# Create the DimSurveys table
df['answer'] = df['selected_answer_id'].combine_first(df['numeric_answer'].astype(str))
fact_responses = df[['user_id', 'survey_id', 'question_id', 'answered_at', 'answer']].drop_duplicates()


# Save the DimSurveys dataframe to a CSV file
output_path_surveys = destination_folder + '/fact_responses.csv'
fact_responses.to_csv(output_path_surveys, index=False)

print(f"fact_responses dataframe has been saved to {output_path_surveys}")