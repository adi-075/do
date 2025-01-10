from pathlib import Path
# Import the file_organize function
from organizer.file_organizer import file_organize
import argparse  # Parse CLI arguments


def main() -> None:
    """
    Entry point for do. 

    Returns:
        None
    """
    # Set up CLI argument parsing
    parser = argparse.ArgumentParser(
        description="Organize files in your Downloads folder with do.")
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        # Defaults to the Operating System's Downloads directory
        default=str(Path.home() / "Downloads"),
        help="The directory to organize. Defaults to the Downloads folder",
    )
    args = parser.parse_args()

    # Get the directory from the CLI arguments
    target_directory = Path(args.directory)

    # Validate that the directory exists
    if not target_directory.exists() or not target_directory.is_dir():
        print(f"Error: {target_directory} is not a valid directory.")
        return

    # Call the file_organize function and pass the target directory
    try:
        file_organize(target_directory)
        print(f"File in {target_directory} have been organized!")
    except ValueError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
