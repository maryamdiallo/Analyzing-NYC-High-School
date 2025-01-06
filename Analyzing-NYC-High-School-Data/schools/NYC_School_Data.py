import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
url = r'C:\Users\diall\PycharmProjects\HighSchoolData\Analyzing-NYC-High-School-Data\schools\hs_directory.csv'
df = pd.read_csv(url)

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Print the columns to ensure correct column names
print(df.columns)

# Data cleaning (if necessary)
# Check for the correct column names
df = df.dropna(subset=['sat_score', 'graduation_rate'])  # Adjust column names if needed
df['sat_score'] = df['sat_score'].astype(float)

# Analyze average SAT scores by school
avg_sat_by_school = df.groupby('school_name')['sat_score'].mean().sort_values(ascending=False)

# Visualize the average SAT scores by school
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_sat_by_school.index, y=avg_sat_by_school.values)
plt.xticks(rotation=90)
plt.title('Average SAT Scores by School')
plt.xlabel('School')
plt.ylabel('Average SAT Score')
plt.show()

# Scatter plot for graduation rate vs SAT scores
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='graduation_rate', y='sat_score')
plt.title('Graduation Rate vs SAT Score')
plt.xlabel('Graduation Rate')
plt.ylabel('SAT Score')
plt.show()

# Heatmap for correlation between numeric variables
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
