import csv
import json
import os

def convert_csv_to_js():
    csv_path = 'Email Project with Data for Alumni Database - Job & Internship Acceptances.csv'
    
    people = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Only include rows with valid data
            if row['Full Name'] and row['Job Title'] and row['Employer']:
                people.append({
                    'Full Name': row['Full Name'],
                    'Job Title': row['Job Title'],
                    'Employer': row['Employer'],
                    'Google Search Query': row['Google Search Query']
                })
    
    # Create JavaScript array
    js_code = "const people = " + json.dumps(people, indent=4) + ";"
    
    # Write to file
    with open('people_data.js', 'w') as f:
        f.write(js_code)
    
    print(f"Converted {len(people)} people to JavaScript format")
    print("Data saved to people_data.js")
    print("\nTo use this in your HTML file:")
    print("1. Replace the people array in index.html with the contents of people_data.js")
    print("2. Or add: <script src='people_data.js'></script> to your HTML")

if __name__ == '__main__':
    convert_csv_to_js() 