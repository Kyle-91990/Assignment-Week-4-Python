import unittest
from unittest.mock import patch, mock_open
from src.utils.file_operations import read_file, write_file

class TestFileOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="test data")
    def test_read_file_success(self, mock_file):
        content = read_file("test.txt")
        self.assertEqual(content, "test data")
        mock_file.assert_called_once_with("test.txt", "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            read_file("non_existent.txt")

    @patch("builtins.open", side_effect=IOError)
    def test_read_file_io_error(self, mock_file):
        with self.assertRaises(IOError):
            read_file("unreadable.txt")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_file_success(self, mock_file):
        write_file("output.txt", "some content")
        mock_file().write.assert_called_once_with("some content")
        mock_file.assert_called_once_with("output.txt", "w")

    @patch("builtins.open", side_effect=IOError)
    def test_write_file_io_error(self, mock_file):
        with self.assertRaises(IOError):
            write_file("unwritable.txt", "content")

if __name__ == "__main__":
    unittest.main()