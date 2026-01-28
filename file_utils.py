
"""
Utility functions related to file operations.
"""

def copy_file(source, destination):
    """
    Copies content from source file to destination file.

    Args:
        source (str): Path of source file
        destination (str): Path of destination file
    """
    with open(source, "r") as src:
        content = src.read()

    with open(destination, "w") as dest:
        dest.write(content)
