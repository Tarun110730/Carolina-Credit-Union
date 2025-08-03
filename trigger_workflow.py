#!/usr/bin/env python3
"""
Script to manually trigger GitHub Actions workflow
Use this when you want to force a sync without changing the CSV
"""

import subprocess
import sys

def trigger_workflow():
    """Trigger the GitHub Actions workflow manually"""
    try:
        # Make a small change to the CSV to trigger the workflow
        print("🔄 Triggering GitHub Actions workflow...")
        
        # Add a comment to the CSV (this will trigger the workflow)
        csv_path = 'Email Project with Data for Alumni Database - Job & Internship Acceptances (1).csv'
        
        # Read the first line to preserve header
        with open(csv_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
        
        # Add a comment line at the top (this will trigger the workflow)
        with open(csv_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add a timestamp comment
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = f"# Last updated: {timestamp}\n"
        
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write(comment + content)
        
        # Commit and push
        subprocess.run(['git', 'add', csv_path], check=True)
        subprocess.run(['git', 'commit', '-m', f'Trigger workflow: {timestamp}'], check=True)
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Successfully triggered GitHub Actions workflow!")
        print("📊 Check the Actions tab in your GitHub repo to see the progress")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def show_status():
    """Show current git status"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        print("📊 Current Git Status:")
        print(result.stdout)
    except Exception as e:
        print(f"❌ Error checking status: {e}")

if __name__ == '__main__':
    print("🔄 GitHub Actions Workflow Trigger")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Trigger workflow (force sync)")
        print("2. Show git status")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            trigger_workflow()
        elif choice == "2":
            show_status()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.") 