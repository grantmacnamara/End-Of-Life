import json
import requests
import os


file_path=r"C:\Users\grant\development\applications.json"
# Read the contents of the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Display the data
print(data)

# API endpoint
API_ENDPOINT = "https://endoflife.date/api/{}.json"

# Dictionary to store results
api_results = {}

# Directory to save JSON files
output_directory = r"C:\Users\grant\development/api_responses/"

# Iterate over each element in data
for item in data:
    application = item.lower()  # Ensure the application name is lowercase
    
    # Construct the filename
    filename = f"{output_directory}{application}.json"
    
    # Check if the file exists
    if os.path.exists(filename):
        print(f"Skipping {filename} as file already exists.")
        continue
    
    # Make the API request
    api_url = API_ENDPOINT.format(application)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Write the response data to a JSON file
        with open(filename, 'w') as outfile:
            json.dump(response.json(), outfile, indent=4)
            
        print(f"Saved data for {application} to {filename}")
    else:
        print(f"Failed to fetch data for {item}")