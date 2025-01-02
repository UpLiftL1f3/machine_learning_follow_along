import os
import sys


def main():
    # Combine all arguments into one path (handles spaces in file paths)
    full_file_path = " ".join(sys.argv[1:])
    if not full_file_path:
        print("Error: No file path provided.")
        sys.exit(1)

    # Normalize the file path to avoid issues with slashes
    full_file_path = os.path.normpath(full_file_path)

    # Find the "AI Learning" directory in the path
    try:
        parts = full_file_path.split(os.sep)
        ai_index = parts.index("AI Learning")  # Look for "AI Learning" in the path
    except ValueError:
        print(
            f"Error: 'AI Learning' directory not found in the file path: {full_file_path}"
        )
        sys.exit(1)

    # Create the module path by converting the relative path to dotted notation
    module_parts = parts[ai_index + 1 :]  # Get parts after "AI Learning"
    module_path = ".".join(module_parts).replace(".py", "")

    # Generate the command
    command = f"python -m {module_path}"
    print(f"Executing: {command}")

    # Execute the command in the terminal
    os.system(command)


if __name__ == "__main__":
    main()
