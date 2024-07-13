import pandas as pd

# Load the CSV file into a DataFrame
source_file = '../data/etl_results/flattened_survey_data.csv'
destination_folder = '../data/star_tables'
df = pd.read_csv(source_file)

# Create the DimSurveys table
dim_surveys = df[['survey_id', 'survey_creation_time']].drop_duplicates()

# Save the DimSurveys dataframe to a CSV file
output_path_surveys = destination_folder + '/DimSurveys.csv'
dim_surveys.to_csv(output_path_surveys, index=False)

print(f"DimSurveys dataframe has been saved to {output_path_surveys}")