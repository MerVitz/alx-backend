#!/usr/bin/env python3
"""
Basic Flask app for Task 0
This script initializes a simple Flask application with one route
and a basic HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)
