# 📊 CSV Editor - Easy Data Management

A user-friendly web-based CSV editor that allows non-technical users to manage alumni data and automatically sync changes to GitHub.

## 🎯 What This Solves

- **No technical knowledge required** - Everything is done through a web interface
- **Automatic Git operations** - No need to manually commit and push
- **Real-time updates** - Changes are immediately reflected
- **Bulk operations** - Manage multiple people at once
- **Search and filter** - Easily find specific people
- **Export/Import** - Backup and restore data easily

## 🚀 Quick Start

### Option 1: Web-Based Editor (Recommended)

1. **Start the server:**
   ```bash
   python start_editor.py
   ```

2. **Open your web browser:**
   - Go to: `http://localhost:5000`
   - The CSV editor will open automatically

3. **Start managing your data:**
   - View all people in a table format
   - Search and filter people
   - Mark people as contacted/available
   - Edit individual records
   - Use bulk operations for multiple people

### Option 2: GitHub Pages (Static)

If you prefer to use the static version on GitHub Pages:

1. **Use the existing GitHub Pages setup:**
   - Go to your GitHub Pages URL
   - Use the main `index.html` for email generation
   - Use `admin_panel.html` for data management

## 📋 Features

### 🔍 Search and Filter
- **Search by name, job title, or employer**
- **Filter by status** (All, Available, Contacted)
- **Real-time search** as you type

### 👥 Individual Management
- **Edit person details** in a modal popup
- **Mark as contacted/available** with one click
- **View all information** in a clean table format

### ⚡ Bulk Operations
- **Select multiple people** using checkboxes
- **Mark selected as contacted/available**
- **Select all/Deselect all** for quick operations
- **Reset all statuses** if needed

### 🔄 Sync Management
- **One-click sync to GitHub** - Updates CSV and pushes to Git
- **Export current data** - Download CSV backup
- **Import new data** - Upload updated CSV files
- **Automatic people_data.js update** - Keeps everything in sync

### 📊 Statistics Dashboard
- **Total people count**
- **Available people count**
- **Contacted people count**
- **Last sync timestamp**

## 🛠️ Technical Details

### Files Overview

- **`csv_editor.html`** - Main web interface
- **`api_server.py`** - Backend API server
- **`start_editor.py`** - Easy startup script
- **`requirements_api.txt`** - Python dependencies

### API Endpoints

- `GET /api/people` - Get all people data
- `POST /api/update_csv` - Update CSV with new data
- `POST /api/sync_to_github` - Sync changes to GitHub
- `GET /api/export_csv` - Download current CSV
- `POST /api/import_csv` - Upload new CSV file
- `GET /api/stats` - Get statistics

### Data Flow

1. **Load data** from CSV file
2. **Display in web interface** with search/filter
3. **User makes changes** (edit, mark status, etc.)
4. **Update CSV file** via API
5. **Sync to GitHub** automatically
6. **Update people_data.js** for GitHub Pages

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- Git repository with proper permissions

### Setup
1. **Clone your repository:**
   ```bash
   git clone <your-repo-url>
   cd Credit Union Coding
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements_api.txt
   ```

3. **Start the editor:**
   ```bash
   python start_editor.py
   ```

## 📖 Usage Guide

### Managing People

1. **View People:**
   - All people are displayed in a table
   - Use search box to find specific people
   - Use filter tabs to show only available/contacted people

2. **Edit a Person:**
   - Click the "Edit" button next to any person
   - Modify their details in the popup form
   - Click "Save Changes" to update

3. **Mark Status:**
   - Click "Mark Contacted" to mark as contacted
   - Click "Mark Available" to mark as available
   - Status is immediately updated

### Bulk Operations

1. **Select Multiple People:**
   - Check the boxes next to people you want to modify
   - Use "Select All" or "Deselect All" for quick selection

2. **Bulk Status Changes:**
   - Select people using checkboxes
   - Click "Mark Selected as Contacted" or "Mark Selected as Available"
   - All selected people will be updated at once

### Syncing to GitHub

1. **Automatic Sync:**
   - Click "Sync to GitHub" button
   - The system will:
     - Update the CSV file
     - Update people_data.js
     - Commit changes to Git
     - Push to GitHub

2. **Export/Import:**
   - Click "Export CSV" to download current data
   - Click "Import CSV" to upload new data
   - Changes are automatically applied

## 🔒 Security Notes

- **Local server only** - The API server runs locally
- **No external dependencies** - Everything is self-contained
- **Git operations** - Uses your local Git credentials
- **File permissions** - Ensure proper file permissions for CSV access

## 🐛 Troubleshooting

### Common Issues

1. **"Port 5000 already in use":**
   - Close other applications using port 5000
   - Or modify the port in `api_server.py`

2. **"Git authentication error":**
   - Ensure Git is configured with your credentials
   - Check repository permissions

3. **"CSV file not found":**
   - Ensure the CSV file exists in the directory
   - Check file permissions

4. **"Dependencies not installed":**
   - Run: `pip install -r requirements_api.txt`
   - Or use: `python start_editor.py` (auto-installs)

### Getting Help

1. **Check the console output** for error messages
2. **Verify file permissions** for CSV and Git operations
3. **Ensure Python dependencies** are installed
4. **Check Git configuration** for authentication

## 🎉 Benefits

### For Non-Technical Users
- **No command line required** - Everything is web-based
- **Intuitive interface** - Easy to understand and use
- **Automatic operations** - No manual Git commands needed
- **Real-time feedback** - See changes immediately

### For Technical Users
- **API-based architecture** - Easy to extend and modify
- **Git integration** - Automatic version control
- **CSV compatibility** - Works with existing data
- **Modular design** - Easy to customize

## 🔄 Workflow

1. **Start the editor** with `python start_editor.py`
2. **Open web browser** to `http://localhost:5000`
3. **Search and filter** people as needed
4. **Make changes** (edit, mark status, bulk operations)
5. **Sync to GitHub** with one click
6. **Stop the server** with Ctrl+C when done

This system provides a complete solution for managing alumni data without requiring technical knowledge, while maintaining the benefits of Git version control and GitHub Pages hosting. 