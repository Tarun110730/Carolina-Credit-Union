#!/usr/bin/env python3
"""
Simple API server for CSV management
Handles CSV updates and Git operations for the web-based editor
"""

from flask import Flask, request, jsonify, send_from_directory
try:
    from flask_cors import CORS
except ImportError:
    print("Warning: flask_cors not found. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "flask-cors"])
    from flask_cors import CORS
import csv
import json
import subprocess
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Configuration
CSV_FILE = 'Email Project with Data for Alumni Database - Job & Internship Acceptances (1).csv'
JS_FILE = 'people_data.js'
REPO_PATH = '.'  # Current directory

@app.route('/')
def index():
    """Serve the main CSV editor"""
    return send_from_directory('.', 'csv_editor.html')

@app.route('/api/people')
def get_people():
    """Get all people from CSV"""
    try:
        people = []
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                people.append({
                    'Full Name': row.get('Full Name', ''),
                    'Job Title': row.get('Job Title', ''),
                    'Employer': row.get('Employer', ''),
                    'Google Search Query': row.get('Google Search Query', ''),
                    'Status': row.get('Status', '')
                })
        return jsonify({'success': True, 'people': people})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/update_csv', methods=['POST'])
def update_csv():
    """Update CSV with new data"""
    try:
        data = request.json
        people = data.get('people', [])
        
        # Read existing CSV to get all columns
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
        
        # Write updated CSV
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for person in people:
                row = {
                    'Class Year': '2013',
                    'Employer': person.get('Employer', ''),
                    'Employer City': 'City',
                    'Employer State': 'State',
                    'Employer Country': 'USA',
                    'Type': 'Full-Time',
                    'Job Title': person.get('Job Title', ''),
                    'Full Name': person.get('Full Name', ''),
                    'Post-Graduation Email Address': 'email@example.com',
                    'Google Search Query': person.get('Google Search Query', ''),
                    'Reachout Notes': '',
                    'Status': person.get('Status', '')
                }
                writer.writerow(row)
        
        # Update people_data.js
        update_js_file(people)
        
        return jsonify({'success': True, 'message': 'CSV updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/sync_to_github', methods=['POST'])
def sync_to_github():
    """Sync changes to GitHub"""
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True, cwd=REPO_PATH)
        
        # Commit with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-sync: Updated CSV data - {timestamp}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True, cwd=REPO_PATH)
        
        # Push to GitHub
        subprocess.run(['git', 'push'], check=True, cwd=REPO_PATH)
        
        return jsonify({
            'success': True, 
            'message': 'Successfully synced to GitHub',
            'timestamp': timestamp
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': f'Git error: {e}'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/export_csv')
def export_csv():
    """Export current CSV data"""
    try:
        return send_from_directory('.', CSV_FILE, as_attachment=True)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/import_csv', methods=['POST'])
def import_csv():
    """Import CSV file"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        # Save uploaded file
        file.save(CSV_FILE)
        
        # Update people_data.js
        people = []
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                people.append({
                    'Full Name': row.get('Full Name', ''),
                    'Job Title': row.get('Job Title', ''),
                    'Employer': row.get('Employer', ''),
                    'Google Search Query': row.get('Google Search Query', ''),
                    'Status': row.get('Status', '')
                })
        
        update_js_file(people)
        
        return jsonify({'success': True, 'message': 'CSV imported successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def update_js_file(people):
    """Update people_data.js with new data"""
    js_content = 'const people = ' + json.dumps(people, indent=2) + ';'
    
    with open(JS_FILE, 'w', encoding='utf-8') as jsfile:
        jsfile.write(js_content)

@app.route('/api/stats')
def get_stats():
    """Get statistics about the data"""
    try:
        people = []
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                people.append(row)
        
        total = len(people)
        available = len([p for p in people if not p.get('Status') or p.get('Status').strip() == ''])
        contacted = total - available
        
        return jsonify({
            'success': True,
            'stats': {
                'total': total,
                'available': available,
                'contacted': contacted
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting CSV Editor API Server...")
    print("📊 CSV File:", CSV_FILE)
    print("🌐 Server will be available at: http://localhost:5000")
    print("📝 CSV Editor will be available at: http://localhost:5000/csv_editor.html")
    print("\nPress Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 