import pandas as pd

# Load the data
norm_category_df = pd.read_csv('Norm_Category.csv', delimiter=';')
norm_keyword_df = pd.read_csv('Norm_Keyword.csv', delimiter=';')
keywords_cat_df = pd.read_csv('Keywords_Cat.csv', delimiter=';')

# Function to list all available categories
def list_categories():
    return norm_category_df['Category'].unique()

# Function to list all standards for a selected category
def list_standards_for_category(category):
    return norm_category_df[norm_category_df['Category'] == category]['Norm'].unique()

# Example usage
print("Available Categories:")
print(list_categories())

selected_category = "Risk"
print(f"\nStandards for {selected_category}:")
print(list_standards_for_category(selected_category))

