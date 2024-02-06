# Load the data
import pandas as pd
norm_category_df = pd.read_csv('Norm_Category.csv', delimiter=';')
norm_keyword_df = pd.read_csv('Norm_Keyword.csv', delimiter=';')
keywords_cat_df = pd.read_csv('Keywords_Cat.csv', delimiter=';')

# Function to list all available categories
def list_categories():
    return norm_category_df['Category'].unique()

# Function to list all available categories
def list_keywords():
    return norm_keyword_df['Key Words'].unique()

# Function to list all standards for a selected Keyword
def list_standards_for_keyword(keyword):
    return norm_keyword_df[norm_keyword_df['Key Words'] == keyword]['Norm'].unique()

# Function to list all standards for a selected category
def list_standards_for_category(category):
    return norm_category_df[norm_category_df['Category'] == category]['Norm'].unique()

# print categories
print("Available Categories:")
print(list_categories())

# print standards for risk category
selected_category = "Risk"
print(f"\nStandards for {selected_category} category:")
print(list_standards_for_category(selected_category))

# print keywords
print("Available Keywords:")
print(list_keywords())


# print standards for risk category
selected_keyword = "mechanical hazards"
print(f"\nStandards for {selected_keyword} keyword:")
print(list_standards_for_keyword(selected_keyword))
