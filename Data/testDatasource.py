import unittest
from datasource import *


class DataSourceTester(unittest.TestCase):
    def setup(self):
        self.ds = DataSource()

    def test_getEdited_true(self,ds):
        for result in self.ds.getEdited(input):
            self.assertEqual(result[9],'TRUE')

    def test_getEdited_false(self):
        for result in self.ds.getEdited(input):
            self.assertEqual(result[9],'FALSE')

    def test_getEdited_otherString(self):
        input = "random"
        self.assertEqual(self.ds.getEdited(input),None)

    def test_getEdited_notString(self):
        input = 2
        self.assertEqual(self.ds.getEdited(input),None)

    def test_getEdited_blank(self):
        input = ''
        self.assertEqual(self.ds.getEdited(input),None)

    def test_getEdited_multinput(self):
        input = list(1,2)
        self.assertEqual(self.ds.getEdited(input),None)

if __name__ == '__main__':
    unittest.main()
