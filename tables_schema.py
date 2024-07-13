import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyBboxPatch

# Define the tables and their columns
tables = {
    'FactResponses': ['user_id', 'survey_id', 'question_id', 'answered_at', 'answer'],
    'DimUsers': ['user_id'],
    'DimSurveys': ['survey_id', 'survey_creation_time'],
    'DimQuestions': ['question_id', 'type', 'subtype', 'question_created_at', 'question_updated_at']
}

# Define the relationships
relationships = {
    'FactResponses': {
        'DimUsers': 'user_id',
        'DimSurveys': 'survey_id',
        'DimQuestions': 'question_id'
    }
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Define positions for the tables
positions = {
    'FactResponses': (0.5, 0.5),
    'DimUsers': (0.1, 0.8),
    'DimSurveys': (0.9, 0.8),
    'DimQuestions': (0.5, 0.1),
}

# Draw the tables with columns
for table, pos in positions.items():
    cols = tables[table]
    text = f"{table}\n" + "\n".join(cols)
    ax.text(pos[0], pos[1], text, bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'),
            ha='center', va='center', fontsize=10, fontweight='bold', family='monospace')

# Draw the connections (arrows)
arrowprops = dict(facecolor='black', arrowstyle='->', lw=2)
for fact, dims in relationships.items():
    for dim, key in dims.items():
        ax.annotate('', xy=positions[dim], xytext=positions[fact], arrowprops=arrowprops)

# Draw the key labels on the connecting lines
for fact, dims in relationships.items():
    for dim, key in dims.items():
        start_pos = positions[fact]
        end_pos = positions[dim]
        mid_pos = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
        ax.text(mid_pos[0], mid_pos[1], key, fontsize=9, fontweight='bold', ha='center', va='center', color='red')

# Set the axis limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Show the plot
plt.title('Star Schema Diagram')
plt.show()