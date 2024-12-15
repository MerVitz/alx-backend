#!/usr/bin/env python3
"""
Flask app with Babel and locale detection for Task 2.
This script initializes Flask, sets up Babel, and detects locale based on request headers.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index page."""
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(debug=True)
