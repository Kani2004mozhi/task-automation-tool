"""
Validates task configuration before execution.
"""

import os

def validate_task(config):
    """
    Validates whether required fields and files exist.

    Args:
        config (dict): Task configuration

    Raises:
        FileNotFoundError: If source file does not exist
    """
    if "source" not in config or "destination" not in config:
        raise ValueError("Invalid task configuration")

    if not os.path.exists(config["source"]):
        raise FileNotFoundError("Source file not found")

