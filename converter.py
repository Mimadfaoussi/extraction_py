import pandas as pd
import json

# Load the data from the JSON file
with open("extracted_data.json", "r") as json_file:
    data = json.load(json_file)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
df.to_excel("extracted_data.xlsx", index=False)

