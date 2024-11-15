import requests
import pandas as pd

# Step (i): Brief description of the API data
print("This script interacts with the Nager.Date API to provide information on public holidays in Austria for 2024.\n")

# Step (a): Fetch data from the API
url = "https://date.nager.at/api/v3/publicholidays/2024/AT"
response = requests.get(url)
if response.status_code == 200:
    holidays_data = response.json()
    # Convert to DataFrame for easy querying
    holidays_df = pd.DataFrame(holidays_data)
    
    # Display columns that can be queried
    print("The data contains the following variables you can query on:")
    print(list(holidays_df.columns))  # Step (b): List available variables
else:
    print("Failed to retrieve data from the API.")
    exit()

# Function to display filtered results
def display_filtered_results(df, column, value):
    filtered_df = df[df[column].astype(str).str.contains(value, case=False, na=False)]
    if filtered_df.empty:
        print("No results found.")
    else:
        print("\nResults:")
        print(filtered_df[['date', 'localName', 'name', 'countryCode', 'type']].to_string(index=False))  # Display selected columns

# Step (e): Allow user to try multiple times
while True:
    # Prompt for column to query
    column_name = input("\nEnter the column name to filter by (or type 'exit' to quit): ")
    if column_name.lower() == 'exit':
        break
    if column_name not in holidays_df.columns:
        print("Invalid column name. Please try again.")
        continue

    # Prompt for value to filter on
    filter_value = input(f"Enter the value to search in column '{column_name}': ")

    # Display results of the query
    display_filtered_results(holidays_df, column_name, filter_value)
