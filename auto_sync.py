#!/usr/bin/env python3
"""
Auto-sync script that updates CSV and pushes to GitHub
Run this after using the app to delete people
"""

import csv
import os
import subprocess
import sys
from update_csv_status import update_csv_status, clear_csv_status, batch_update_csv

def git_push():
    """Push changes to GitHub"""
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', 'Auto-sync: Updated CSV status'], check=True)
        
        # Push to GitHub
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Successfully pushed changes to GitHub!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error pushing to GitHub: {e}")
        return False

def convert_csv_to_js():
    """Convert CSV to JavaScript data"""
    try:
        subprocess.run([sys.executable, 'convert_csv_to_js.py'], check=True)
        print("✅ Converted CSV to JavaScript data")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting CSV: {e}")
        return False

def auto_sync_workflow():
    """Complete auto-sync workflow"""
    print("🔄 Auto-Sync Workflow")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Mark person as 'Reachout Sent' and push")
        print("2. Clear person's status and push")
        print("3. Batch update multiple people and push")
        print("4. Just convert CSV to JS and push")
        print("5. View current status")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            name = input("Enter full name to mark as 'Reachout Sent': ").strip()
            if name:
                update_csv_status(name)
                if convert_csv_to_js() and git_push():
                    print(f"✅ Complete! {name} marked as 'Reachout Sent' and pushed to GitHub")
        
        elif choice == "2":
            name = input("Enter full name to clear status: ").strip()
            if name:
                clear_csv_status(name)
                if convert_csv_to_js() and git_push():
                    print(f"✅ Complete! Cleared status for {name} and pushed to GitHub")
        
        elif choice == "3":
            print("Enter names (one per line, press Enter twice when done):")
            names = []
            while True:
                name = input().strip()
                if not name:
                    break
                names.append(name)
            
            if names:
                batch_update_csv(names)
                if convert_csv_to_js() and git_push():
                    print(f"✅ Complete! Updated {len(names)} people and pushed to GitHub")
        
        elif choice == "4":
            if convert_csv_to_js() and git_push():
                print("✅ Complete! Converted CSV and pushed to GitHub")
        
        elif choice == "5":
            show_status()
        
        elif choice == "6":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

def show_status():
    """Show current status of people"""
    csv_path = 'Email Project with Data for Alumni Database - Job & Internship Acceptances (1).csv'
    
    if not os.path.exists(csv_path):
        print("❌ CSV file not found!")
        return
    
    available = 0
    contacted = 0
    
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Full Name'] and row['Job Title'] and row['Employer']:
                if row.get('Status') and row['Status'].strip() == 'Reachout Sent':
                    contacted += 1
                else:
                    available += 1
    
    print(f"\n📊 Current Status:")
    print(f"   Available: {available} people")
    print(f"   Contacted: {contacted} people")
    print(f"   Total: {available + contacted} people")

if __name__ == '__main__':
    auto_sync_workflow() 