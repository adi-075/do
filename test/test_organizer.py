import unittest
import tempfile
import shutil
from pathlib import Path
from organizer.file_organizer import file_organize

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        # Set up a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.images_dir = Path(self.test_dir) / "Images"
        self.documents_dir = Path(self.test_dir) / "Documents"
        self.images_dir.mkdir(exist_ok=True)
        self.documents_dir.mkdir(exist_ok=True)
        
        # Create sample files
        self.image_file = Path(self.test_dir) / "test_image.jpg"
        self.document_file = Path(self.test_dir) / "test_document.pdf"
        
        self.image_file.touch()  # Create a dummy file
        self.document_file.touch()  # Create a dummy file

    def test_organize_files(self):
        # Run the file_organize function
        file_organize(Path(self.test_dir))
        
        # Assert the files were moved to the correct directories
        self.assertTrue(self.images_dir / "test_image.jpg" in Path(self.test_dir).glob('**/*'))
        self.assertTrue(self.documents_dir / "test_document.pdf" in Path(self.test_dir).glob('**/*'))

    def tearDown(self):
        # Remove the temporary directory and its contents after the test
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
