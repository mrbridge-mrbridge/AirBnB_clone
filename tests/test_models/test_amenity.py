#!/usr/bin/python3
"""
Test Amenity
"""

from datetime import datetime
import inspect
from models import Amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenityz = Amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenityz class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenityz, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/Amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/Amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the Amenity.py module docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity.py needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenityz class docstring"""
        self.assertIsNot(Amenityz.__doc__, None,
                         "Amenityz class needs a docstring")
        self.assertTrue(len(Amenityz.__doc__) >= 1,
                        "Amenityz class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenityz methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenityz class"""
    def test_is_subclass(self):
        """Test that Amenityz is a subclass of BaseModel"""
        Amenity = Amenityz()
        self.assertIsInstance(Amenity, BaseModel)
        self.assertTrue(hasattr(Amenity, "id"))
        self.assertTrue(hasattr(Amenity, "created_at"))
        self.assertTrue(hasattr(Amenity, "updated_at"))

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenityz()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenityz")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        Amenity = Amenityz()
        string = "[Amenityz] ({}) {}".format(Amenity.id, Amenity.__dict__)
        self.assertEqual(string, str(Amenity))

    def test_name_attr(self):
        """Test that Amenityz has attribute name,
         and it's as an empty string"""
        Amenity = Amenityz()
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertEqual(Amenity.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenityz()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenityz()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenityz")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))


if __name__ == '__main__':
    unittest.main()
