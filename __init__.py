import pandas as pd

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

# Read Excel file into DataFrame
df = pd.read_excel('MayShiftRoster.xlsx')

# Specify the specific name
specific_name = 'surendhirakumar.ravichandran'

# Call the function and print the result
result = get_date_values_pairs(df, specific_name)
print(result)


def get_keys_by_values(dictionary, desired_values):
    keys_by_values = {value: [] for value in desired_values}
    for key, val in dictionary.items():
        if val in desired_values:
            keys_by_values[val].append(key)
    return keys_by_values

desired_values = ['S1','S2','S3']
keys_by_values = get_keys_by_values(result, desired_values)
print(keys_by_values)