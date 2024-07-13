import pandas as pd

# Load the CSV file into a DataFrame
source_file = '../data/etl_results/flattened_survey_data.csv'
destination_folder = '../data/star_tables'
df = pd.read_csv(source_file)

# Create the DimQuestions table
dim_questions = df[['question_id', 'type', 'subtype', 'question_created_at', 'question_updated_at']].drop_duplicates()

# Save the DimQuestions dataframe to a CSV file
output_path_questions = destination_folder + '/dim_questions.csv'
dim_questions.to_csv(output_path_questions, index=False)

print(f"DimQuestions dataframe has been saved to {output_path_questions}")