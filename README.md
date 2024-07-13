# Raven Data Project

This repository contains the necessary scripts and data for the Raven Data project, which involves processing health survey data to generate a star schema for analysis and dashboard.

## Project Structure

```
.
├── .idea
│   ├── inspectionProfiles
│   ├── .gitignore
│   ├── misc.xml
│   ├── modules.xml
│   ├── other.xml
│   ├── Raven Data.iml
│   ├── ruff.xml
│   └── workspace.xml
├── data
│   ├── etl_results
│   │   └── flattened_survey_data.csv
│   ├── raw_data
│   │   └── Health Survey Results.csv
│   └── star_tables
│       ├── dim_questions.csv
│       ├── DimSurveys.csv
│       ├── DimUsers.csv
│       └── fact_responses.csv
├── preprocess
│   ├── preprocess_fact.py
│   ├── preprocess_questions.py
│   ├── preprocess_survey.py
│   ├── preprocess_users.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── ETL.py
│   ├── Health Survey Dashboard task.pdf
│   └── tables_schema.py
```

## Setup Instructions

### Prerequisites

- Python 3.11.0

### Running the ETL Process

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the ETL Script**

   Navigate to the `preprocess` directory and run the ETL script:

   ```bash
   cd preprocess
   python ETL.py
   ```

   This script will process the raw health survey data and save the flattened survey data in the `etl_results` directory.

### Running the Preprocessing Scripts

After running the ETL script, you need to run the preprocessing scripts to create the star schema.

```bash
python preprocess_fact.py
python preprocess_questions.py
python preprocess_survey.py
python preprocess_users.py
```

### Creating the Schema

Finally, run the `tables_schema.py` script to create the database schema:

```bash
python tables_schema.py
```

## Additional Resources

For a detailed explanation of the work process, please refer to the [Notion page](https://pickle-fuel-2bd.notion.site/MindLift-Health-Survey-Dashboard-0aafabbd37ad4cedbfa9b6d3a1a1615d).

The dashboard mockup, created by Claude artifacts, can be found [here](https://claude.site/artifacts/95833586-f83c-4482-942c-0d511a13beb8).
