#!/usr/bin/python3
"""
Test City
"""

from datetime import datetime
import inspect
import models
from models import City
from models.base_model import Basemodel
import pep8
import unittest
Cityx = City.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Cityx class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(Cityx, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/City.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/City.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the City.py module docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City.py needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the Cityx class docstring"""
        self.assertIsNot(Cityx.__doc__, None,
                         "Cityx class needs a docstring")
        self.assertTrue(len(Cityx.__doc__) >= 1,
                        "Cityx class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in Cityx methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test the Cityx class"""
    def test_is_subclass(self):
        """Test that Cityx is a subclass of Basemodel"""
        City = Cityx()
        self.assertIsInstance(City, Basemodel)
        self.assertTrue(hasattr(City, "id"))
        self.assertTrue(hasattr(City, "created_at"))
        self.assertTrue(hasattr(City, "updated_at"))

    def test_name_attr(self):
        """Test that Cityx has attribute name, and it's an empty string"""
        City = Cityx()
        self.assertTrue(hasattr(City, "name"))
        if models.storage_t == 'db':
            self.assertEqual(City.name, None)
        else:
            self.assertEqual(City.name, "")

    def test_state_id_attr(self):
        """Test that Cityx has attribute state_id, and it's an empty string"""
        City = Cityx()
        self.assertTrue(hasattr(City, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(City.state_id, None)
        else:
            self.assertEqual(City.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = Cityx()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Cityx()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Cityx")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        City = Cityx()
        string = "[Cityx] ({}) {}".format(City.id, City.__dict__)
        self.assertEqual(string, str(City))


if __name__ == '__main__':
    unittest.main()
