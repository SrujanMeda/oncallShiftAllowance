import pandas as pd

# Read Excel file into DataFrame
df = pd.read_excel('MayShiftRoster.xlsx')
unique_names = df['Name'].unique().tolist()

print(unique_names)
def get_date_values_pairs(df, specific_name):
    """
    Function to get the {date: values} pairs for a specific name.
    
    Args:
    - df: DataFrame containing the Excel data
    - specific_name: Name for which the {date: values} pairs are required
    
    Returns:
    - date_values_pairs: Dictionary containing {date: values} pairs for the specified name
    """
    # Filter the DataFrame for the specific name
    specific_name_df = df[df['Name'] == specific_name]

    # Create a dictionary to store the {date: values} pairs
    date_values_pairs = {}

    # Iterate through each row of the filtered DataFrame
    for index, row in specific_name_df.iterrows():
        # Iterate through each column except for 'Name' and 'Team'
        for column in df.columns[3:]:
            # Check if the value is not NaN
            if pd.notna(row[column]):
                # Add the {date: value} pair to the dictionary
                date_values_pairs[column] = row[column]
    
    return date_values_pairs

def get_keys_by_values(dictionary, desired_values):
    keys_by_values = {value: [] for value in desired_values}
    for key, val in dictionary.items():
        if val in desired_values:
            keys_by_values[val].append(key)
    return keys_by_values


# Specify the specific name
for name in unique_names:
    specific_name = name
    # Call the function and print the result
    result = get_date_values_pairs(df, specific_name)
    #print(result)
    desired_values = ['S1','S2','S3']
    keys_by_values = get_keys_by_values(result, desired_values)
    print(specific_name , keys_by_values)