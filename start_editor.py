#!/usr/bin/env python3
"""
Simple startup script for the CSV Editor
For non-technical users to easily start the web-based CSV editor
"""

import os
import sys
import subprocess
import webbrowser
import time

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_cors
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Installing required packages...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_api.txt'], check=True)
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False

def start_server():
    """Start the API server"""
    print("🚀 Starting CSV Editor Server...")
    print("📊 This will start a web-based CSV editor")
    print("🌐 The editor will be available in your web browser")
    print("\nPress Ctrl+C to stop the server when you're done")
    print("=" * 50)
    
    try:
        # Start the API server
        subprocess.run([sys.executable, 'api_server.py'])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    print("📊 CSV Editor - Easy Data Management")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('api_server.py'):
        print("❌ Error: Please run this script from the Credit Union Coding directory")
        print("   Make sure you're in the folder with api_server.py")
        return
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Cannot start server due to missing dependencies")
        return
    
    # Start server
    start_server()

if __name__ == '__main__':
    main() 