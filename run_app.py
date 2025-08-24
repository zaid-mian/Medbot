#!/usr/bin/env python3
import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.main import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)

