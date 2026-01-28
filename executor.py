"""
Executes tasks based on configuration.
"""

from utils.file_utils import copy_file
from core.logger import log

def execute_task(config):
    """
    Executes the task defined in config.

    Args:
        config (dict): Task configuration
    """
    task = config.get("task")

    if task == "backup":
        copy_file(config["source"], config["destination"])
        log("Backup task completed successfully")
    else:
        log("Unknown task")

