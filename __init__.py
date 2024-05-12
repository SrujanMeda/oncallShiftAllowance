import pandas as pd
import datetime

# Read Excel file into DataFrame
df = pd.read_excel('MayShiftRoster.xlsx')
unique_names = df['Name'].unique().tolist()

#print(len(unique_names))
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

def is_weekend(date):
    return date.weekday() >= 5  # Saturday (5) or Sunday (6)

# Specify the specific name
for name in unique_names:
    specific_name = name
    # Call the function and print the result
    result = get_date_values_pairs(df, specific_name)
    #print(result)
    shift_b = []
    shift_c = []
    weekend = []
    desired_values = ['S1','S2','S3']
    keys_by_values = get_keys_by_values(result, desired_values)
    for key, dates in keys_by_values.items():
        for date in dates:
            date_obj = datetime.datetime(2024, 5, date)  # Creating a datetime object may 2024
            if key in ['S1', 'S2', 'S3']:  # Check for all keys
                if is_weekend(date_obj):  # If date is a weekend
                    weekend.append(date)
            if key in ['S1', 'S2']:  # Check for Shift B
                if not is_weekend(date_obj):  # If date is a weekday
                    shift_b.append(date)
            elif key == 'S3':  # Check for Shift C
                if not is_weekend(date_obj):  # If date is a weekday
                    shift_c.append(date)
    shift_b.sort()
    shift_c.sort()
    weekend.sort()
    print(name)                
    print("Shift B:", shift_b)
    print("Shift C:", shift_c)
    print("Weekend:", weekend)