#!/usr/bin/python3
"""Unit testing for the base model"""

import unittest
import pep8
import cmd
from models.base_model import Basemodel


class test_basemodel(unittest.TestCase):
    """Test Model for the Base Model"""
    def test_pep8(self):
        """Tests if the code is pep8 complaint"""
        pycodestlye = pep8.StyleGuide(quiet=True)
        result = pycodestlye.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails Pep8 complaince")

    def test_file(self):
        """Tests if file exists"""
        self.assertTrue(isflie('models/base_model.py'),'File missing' )

class test_dict(unittest.TestCase):
    """Dict Basemodel"""

    def startUp(self):
        '''Set Up'''
        self.dict1 = BaseModel().to_dict()
        self.dict2 = BaseModel().to_dict()

    def test_dict(self):
        self.assertTrue(self.dict1, dict,
        "Failed to generate dictionary" "type")



if __name__ == '__main__':
    unittest.main()
