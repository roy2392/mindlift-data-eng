import pandas as pd
import json

# Load the CSV file
file_path = 'data/raw_data/Health Survey Results.csv'
df = pd.read_csv(file_path)

# Function to parse the survey results JSON and flatten it
def parse_and_flatten(row):
    survey_results = row['survey_results']
    survey_id = row['survey_id']
    survey_creation_time = row['survey_createdat']
    user_id = row['userid']

    parsed_results = []
    survey_data = json.loads(survey_results)
    for question in survey_data['survey_results']:
        parsed_results.append({
            'user_id': user_id,
            'survey_id': survey_id,
            'survey_creation_time': survey_creation_time,
            'question_id': question.get('id'),
            'type': question.get('type'),
            'subtype': question.get('subtype'),
            'question_created_at': question.get('createdAt'),
            'question_updated_at': question.get('updatedAt'),
            'answered_at': question.get('answeredAt'),
            'selected_answer_id': question.get('selectedAnswerId'),
            'numeric_answer': question.get('numericAnswer'),
            'selected_answer_ids': question.get('selectedAnswerIds'),
            'free_text': question.get('freeText')
        })
    return parsed_results

# Apply the function and explode the DataFrame
flat_data = df.apply(parse_and_flatten, axis=1).explode().reset_index(drop=True)
flat_df = pd.DataFrame(flat_data.tolist())

# Save the flattened DataFrame to a new CSV file
flat_df.to_csv('data/etl_results/flattened_survey_data.csv', index=False)

# Show the first few rows of the flattened DataFrame
flat_df.head()


# now each row represent a single question in the survey
