from flask import Flask, render_template
import json
import os
import re

app = Flask(__name__)

# Custom function to extract numeric part of the cycle
def extract_numeric_cycle(cycle):
    numeric_part = re.findall(r'\d+\.\d+', cycle)
    return float(numeric_part[0]) if numeric_part else 0

@app.route('/')
def index():
    # Load application names from applications.json
    with open('applications.json', 'r') as f:
        applications = json.load(f)

    # Collect data for each application
    application_data = []
    for app_name in applications:
        # Load data from corresponding JSON file in api_responses folder
        json_file = os.path.join('api_responses', f'{app_name}.json')
        with open(json_file, 'r') as f:
            app_info = json.load(f)

        # Find the latest release based on highest 'cycle'
        latest_release = max(app_info, key=lambda x: extract_numeric_cycle(x.get('cycle', '0')))

        # Append relevant data to application_data list
        application_data.append({
            'name': app_name,
            'latest_version': latest_release.get('cycle', 'N/A'),
            'release_date': latest_release.get('releaseDate', 'N/A'),
            'end_of_life': latest_release.get('eol', 'N/A')
        })

    # Render HTML template with application data
    return render_template('index.html', applications=application_data)

if __name__ == '__main__':
    app.run(debug=True)
