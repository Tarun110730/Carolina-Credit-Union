import csv
import os

def update_csv_status(full_name, status="Reachout Sent"):
    """
    Update the Status column in the CSV file for a specific person
    """
    csv_path = 'Email Project with Data for Alumni Database - Job & Internship Acceptances (1).csv'
    
    # Read the CSV file
    rows = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        
        for row in reader:
            if row['Full Name'] == full_name:
                row['Status'] = status
            rows.append(row)
    
    # Write back to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Updated {full_name} status to '{status}' in CSV file")

def clear_csv_status(full_name):
    """
    Clear the Status column for a specific person (for undo functionality)
    """
    update_csv_status(full_name, "")

def get_available_people():
    """
    Get list of people who haven't been marked as "Reachout Sent"
    """
    csv_path = 'Email Project with Data for Alumni Database - Job & Internship Acceptances (1).csv'
    
    available_people = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Full Name'] and row['Job Title'] and row['Employer']:
                # Only include people without "Reachout Sent" status
                if not row.get('Status') or row['Status'].strip() == '':
                    available_people.append({
                        'Full Name': row['Full Name'],
                        'Job Title': row['Job Title'],
                        'Employer': row['Employer'],
                        'Google Search Query': row['Google Search Query']
                    })
    
    return available_people

if __name__ == '__main__':
    # Example usage
    print("Available people:")
    available = get_available_people()
    print(f"Total available: {len(available)}")
    
    # Example: Mark someone as "Reachout Sent"
    # update_csv_status("Colin Sullivan")
    
    # Example: Clear someone's status
    # clear_csv_status("Colin Sullivan") 