import combine_csv
import unittest
import sys
import os

PATH = os.path.join(os.getcwd(), 'fixtures')


class TestCombineCsv(unittest.TestCase):


    def test_get_files_names(self):
        sys.argv = ['combine_csv.py', './fixtures/accessories.csv', './fixtures/clothing.csv', './fixtures/household_cleaners.csv', 'combined2.csv']
        files, file_names = combine_csv.get_files()
        test_names = ["accessories.csv", "clothing.csv", "household_cleaners.csv"]
        self.assertEqual(test_names, file_names)


    def test_get_files_paths(self):
        sys.argv = ['combine_csv.py', './fixtures/accessories.csv', './fixtures/clothing.csv', './fixtures/household_cleaners.csv', 'combined2.csv']
        files, file_names = combine_csv.get_files()
        test_paths = [os.path.join(PATH,"accessories.csv"), os.path.join(PATH,"clothing.csv"), os.path.join(PATH,"household_cleaners.csv")]
        self.assertEqual(test_paths, files)
