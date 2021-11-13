#!/usr/bin/python3
"""Unit testing for the base model"""

import unittest
import pep8
import cmd
from models.base_model import Basemodel
from datetime import datetime
from os import remove
from os.path import isfile


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
        self.assertTrue(isfile('models/base_model.py'),'File missing' )

class test_to_dict(unittest.TestCase):
    """Dict Basemodel"""

    def startUp(self):
        '''Set Up'''
        self.dict1 = Basemodel().to_dict()
        self.dict2 = Basemodel().to_dict()

    def test_dict(self):
        self.assertTrue(self.dict1, dict,
        "Failed to generate dictionary" "type")

    def test_method_existence(self):
        '''Test for method existence'''
        classd = dir(__import__('models').base_model.Basemodel)
        self.assertIn('__init__', classd, "Missing __init__ method")
        self.assertIn('__str__', classd, "Missing __str__ method")
        self.assertIn('save', classd, "Missing save method")
        self.assertIn('to_dict', classd, "Missing to_dict method")

    def test_instants(self):
        '''Test for failed instantiation'''
        try:
            oj1 = Basemodel()
            oj2 = Basemodel('Test')
            oj3 = Basemodel('id')
            oj4 = Basemodel(888)

        except:
            self.fail("Failed Basemodel instantiation")
        finally:
            del oj1
            del oj2
            del oj3
            del oj4



    def test_instance_classmatch(self):
        '''Test if instanced object matches class'''
        oj1 = Basemodel()
        self.assertIsInstance(oj1, Basemodel,
        "Instanced object is not Basemodel class")
        del oj1

    def test_attr_exist(self):
        '''Test for public attribute existence'''
        oj1 = Basemodel()
        self.assertIsInstance(oj1.id, str,
                              "Instanced object.id not a string type")
        self.assertIsInstance(oj1.created_at, datetime,
                              "Instanced object.created_at not datetime type")
        self.assertIsInstance(oj1.updated_at, datetime,
                              "Instanced object.updated_at not datetime type")
        del oj1

    def test_dynamicattr(self):
        '''Test to dynamically add attributes'''
        oj1 = Basemodel()
        try:
            oj1.test1 = 'TEST'
            oj1.test2 = [1, 2, 3]
            oj1.test3 = {'a': 1, 'b': 2, 'c': 3}
            oj1.test4 = (4, 5, 6)
            oj1.test5 = {7, 8, 9}
            oj1.test6 = None
            oj1.test7 = 0.0
            oj1.test8 = float('nan')
            oj1.test9 = float('inf')
            oj1.test10 = -666
            oj1.test11 = ''
            oj1.test12 = []
            oj1.test13 = [-5]
            oj1.test14 = {}
            oj1.test15 = {'u': [6, 7]}
        except:
            self.fail("Failed to dynamically add pub inst attributes")
        self.assertEqual(oj1.__dict__['test1'], 'TEST',
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test2'], [1, 2, 3],
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test3'], {'a': 1, 'b': 2, 'c': 3},
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test4'], (4, 5, 6),
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test5'], {7, 8, 9},
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test6'], None,
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test7'], 0.0,
                         "Failed to assign value")
        self.assertNotEqual(oj1.__dict__['test8'], float('nan'),
                            "Failed to assign value")
        self.assertEqual(oj1.__dict__['test9'], float('inf'),
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test10'], -666,
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test11'], '',
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test12'], [],
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test13'], [-5],
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test14'], {},
                         "Failed to assign value")
        self.assertEqual(oj1.__dict__['test15'], {'u': [6, 7]},
                         "Failed to assign value")
        self.assertEqual(len(oj1.__dict__), 18)
        del oj1

class test_str(unittest.TestCase):
    """Tests the str class"""

    @classmethod
    def setUp(cls):
        '''Set Up '''
        cls.oj1 = Basemodel(id="1234-5678-9012",
                             created_at="1234-05-06T01:23:45.678901",
                             updated_at="9999-11-11T11:11:22.222222")
        cls.god1 = '[Basemodel]'
        cls.god2 = '(1234-5678-9012)'

    @classmethod
    def DownClass(cls):
        '''Down'''
        del cls.oj1

    def test_str_return_(self):
        '''Test __str__ return'''
        out = type(self).oj1.__str__()
        self.assertIsInstance(out, str,
                              " __str__ incorrect return ")

    def test_str_format(self):
        '''Test __str__ format'''
        out1 = type(self).oj1.__str__().split(' ', 2)[0]
        out2 = type(self).oj1.__str__().split(' ', 2)[1]
        self.assertEqual(out1, type(self).god1,
                         "Class name does not match ")
        self.assertEqual(out2, type(self).god2,
                         "ID does not match ")

    def test_str_return_dynamic_attr(self):
        '''Test __str__ return with dynamic attr'''
        type(self).oj1.test1 = 'TEST'
        type(self).oj1.test2 = [1, 2, 3]
        out = type(self).oj1.__str__()
        self.assertIsInstance(out, str,
                              "improper __str__ ")

class Test_Basemodel_Constuctor(unittest.TestCase):
    '''Test Basemodel Constructor'''

    @classmethod
    def setUp(cls):
        '''Setup '''
        cls.oj1 = Basemodel()
        cls.oj2 = Basemodel()
        cls.oj3 = Basemodel()

    @classmethod
    def DownClass(cls):
        '''Tear Down Class'''
        del cls.oj1
        del cls.oj2
        del cls.oj3

    def test_key_exist(self):
        '''Test for basic key existence'''
        self.assertIn('id', dir(type(self).oj1), "Missing id key")
        self.assertIn('created_at', dir(type(self).oj1),
                      "Missing created_at key")
        self.assertIn('updated_at', dir(type(self).oj1),
                      "Missing updated_at key")

    def test_id_generator(self):
        '''Test for  generated Ids'''
        self.assertNotEqual(type(self).oj1.id, type(self).oj2.id,
                            "Fail: Alike ID")
        self.assertNotEqual(type(self).oj2.id, type(self).oj3.id,
                            "Fail: Alike ID")
        self.assertNotEqual(type(self).oj1.id, type(self).oj3.id,
                            "Fail: Alike ID")

    def test_03_datetime(self):
        '''Test for same datetime'''
        self.assertEqual(type(self).oj1.created_at,
                         type(self).oj1.updated_at,
                         "Fail: Different time/date")
        self.assertEqual(type(self).oj2.created_at,
                         type(self).oj2.updated_at,
                         "Fail: Different time/date")
        self.assertEqual(type(self).oj3.created_at,
                         type(self).oj3.updated_at,
                         "Fail: Different time/date")




if __name__ == '__main__':
    unittest.main()
