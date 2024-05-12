import datetime

roster = {'S1': [25, 26, 27, 28, 29, 30, 31], 'S2': [3, 14, 15, 16, 20, 21, 22], 'S3': [4, 5, 6, 7, 8, 9, 10]}

shift_b = []
shift_c = []
weekend = []

def is_weekend(date):
    return date.weekday() >= 5  # Saturday (5) or Sunday (6)

for key, dates in roster.items():
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

print("Shift B:", shift_b)
print("Shift C:", shift_c)
print("Weekend:", weekend)
