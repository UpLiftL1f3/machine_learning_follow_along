import os

project_root = "/Users/gilster/Coding/AI Learning"


def print_message(message):
    """
    Prints a message to the terminal and adds a row of stars below it.
    The stars span the full width of the terminal.
    :param message: The message to print, can include f-string formatted values.
    """
    # Get the terminal width
    terminal_width = os.get_terminal_size().columns

    # Print the message
    print(message)

    # Print a full-width row of stars
    print(f"{"*" * terminal_width}\n")


def get_file_path(file_name):
    global project_root
    """
    Searches for the specified file within the main project directory.
    If the file is found, returns the absolute path. Otherwise, raises an error.

    :param file_name: Name of the file to locate
    :param project_root: The root directory of the project to start searching (default: current working directory)
    :return: Full file path if the file exists
    """
    if project_root is None:
        project_root = os.getcwd()

    # Walk through the directory to find the file
    for root, _, files in os.walk(project_root):
        if file_name in files:
            return os.path.join(root, file_name)

    # Raise an error if the file is not found
    raise FileNotFoundError(
        f"Error: File '{file_name}' not found in project: {project_root}"
    )
