from pathlib import Path
import os
import shutil
# Import categories from config.py
from organizer.config import FILE_CATEGORIES


def move_file_with_unique_name(file: Path, target_folder: Path) -> None:
    """
    Moves the file to the target folder, ensuring the filename is unique.
    """
    # Make sure the target folder exists
    target_folder.mkdir(parents=True, exist_ok=True)

    # Check if the file exists
    if not file.exists():
        print(f"File not found: {file}")
        return

    # Handle case-sensitivity and special characters
    target_path = target_folder / file.name

    # Check if the target file already exists and add a index to the filename
    counter = 1
    while target_path.exists():
        target_path = target_folder / f"{file.stem}_{counter}{file.suffix}"
        counter += 1

    print(f"Moving: {file} -> {target_path}")
    shutil.move(str(file), str(target_path))


def file_organize(directory: str | Path) -> None:
    '''
    Organize files in the downloads directory based on their extension.

    Parameters:
        directory (str | Path): Takes the path to your Downloads Directory. Can be a string or a Path object.

    Returns:
        None

    Raises:
        ValueError: If the directory provided is not a valid directory.
    '''
    for file in directory.iterdir():  # Iterate over all the files
        # Skip directories and invisible files
        if file.is_dir() or file.name.startswith('.'):
            continue

        # Log file being checked
        # print(f"Checking file: {file.name} with extension {
        #       file.suffix.lower()}")

        # Handle the file extensions case-insensitively
        for category, extensions in FILE_CATEGORIES.items():
            if file.suffix.lower() in [ext.lower() for ext in extensions]:
                # Move the file to the corresponding category folder
                category_folder = directory / category
                move_file_with_unique_name(file, category_folder)
                break
