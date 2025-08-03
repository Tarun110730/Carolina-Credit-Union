# Cold Email Generator - CSV Synced Version

This version uses the CSV file as the source of truth for tracking which people have been contacted.

## 🎯 **How It Works:**

1. **Status Column Tracking**: Uses the `Status` column in the CSV to mark people as "Reachout Sent"
2. **GitHub Sync**: When you delete someone, their status is updated in the CSV
3. **Filtered Display**: Only shows people without "Reachout Sent" status in the dropdown
4. **Team Coordination**: Everyone sees the same list by pulling the latest CSV from GitHub

## 📁 **Files:**

- `csv_synced_version.html` - The main app
- `convert_csv_to_js.py` - Converts CSV to JavaScript data
- `update_csv_status.py` - Updates CSV status (for manual use)
- `people_data.js` - Generated JavaScript data (run convert script to update)

## 🚀 **Setup Instructions:**

### 1. **Convert CSV to JavaScript:**
```bash
python convert_csv_to_js.py
```

### 2. **Deploy to GitHub Pages:**
- Upload `csv_synced_version.html` as `index.html`
- Upload `people_data.js`
- Enable GitHub Pages in your repo settings

### 3. **Update Process:**
When someone is "deleted" (marked as contacted):
1. The app updates the local data
2. **You need to manually update the CSV** (or use the Python script)
3. **Commit and push to GitHub** for others to see changes

## 🔄 **Workflow:**

### **Option 1: Auto-Sync (Recommended)**
1. Open the app
2. Select a person to contact
3. Click "Delete Selected Person" (marks as "Reachout Sent")
4. Generate and send the email
5. **Run auto-sync script:**
   ```bash
   python auto_sync.py
   ```
6. Choose option 1 to mark the person and push to GitHub

### **Option 2: Manual Sync**
1. Use the app as above
2. Run the sync script:
   ```bash
   python sync_deletions.py
   ```
3. Manually commit and push:
   ```bash
   git add .
   git commit -m "Updated CSV status"
   git push
   ```

### **Option 3: GitHub Actions (Automatic)**
- The `.github/workflows/auto-sync-csv.yml` will automatically:
  - Convert CSV to JavaScript when CSV changes
  - Update `people_data.js` automatically
  - Commit and push changes

## ✅ **Benefits:**

- **Simple**: No Firebase setup required
- **Free**: Uses GitHub for hosting and sync
- **Transparent**: CSV file shows exactly who's been contacted
- **Backup**: CSV serves as a permanent record
- **Team-friendly**: Everyone can see the same status

## ⚠️ **Important Notes:**

1. **Manual CSV Updates**: You must manually update the CSV when deleting people
2. **GitHub Sync**: Changes only appear for others after you commit and push
3. **Backup**: Always backup your CSV before making changes
4. **Status Values**: Use exactly "Reachout Sent" (case sensitive)

## 🔧 **Troubleshooting:**

### **If people aren't showing up:**
- Check that their `Status` column is empty
- Run `convert_csv_to_js.py` to regenerate the data
- Refresh the page

### **If changes aren't syncing:**
- Make sure you committed and pushed the CSV changes
- Check that others have pulled the latest changes
- Verify the CSV file path is correct

## 📊 **Status Tracking:**

- **Empty Status**: Available for contact
- **"Reachout Sent"**: Already contacted, won't show in dropdown
- **Other values**: Can be used for additional tracking (e.g., "Responded", "No Response")

This system provides a simple, free way to coordinate cold email outreach across your team! 