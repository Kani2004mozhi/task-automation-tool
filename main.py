"""
Main entry point of the application.
"""

import json
from core.validator import validate_task
from core.executor import execute_task
from core.logger import log

def load_config():
    """
    Loads task configuration from JSON file.
    """
    with open("config/tasks.json", "r") as file:
        return json.load(file)

def main():
    """
    Orchestrates validation and execution.
    """
    try:
        config = load_config()
        validate_task(config)
        execute_task(config)
    except Exception as e:
        log(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

