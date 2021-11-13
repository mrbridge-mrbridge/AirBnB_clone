#!/usr/bin/python3
"""
Test Userx
"""

from datetime import datetime
import inspect
import models
from models import User
from models.base_model import BaseModel
import pep8
import unittest
Userx = User.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of Userx class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Userx, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/User.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/User.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the User.py module docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User.py needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(Userx.__doc__, None,
                         "Userx class needs a docstring")
        self.assertTrue(len(Userx.__doc__) >= 1,
                        "Userx class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in Userx methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the Userx class"""
    def test_is_subclass(self):
        """Test that Userx is a subclass of BaseModel"""
        User = Userx()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(User, "id"))
        self.assertTrue(hasattr(User, "created_at"))
        self.assertTrue(hasattr(User, "updated_at"))

    def test_email_attr(self):
        """Test that Userx has attr email, and it's an empty string"""
        User = Userx()
        self.assertTrue(hasattr(User, "email"))
        self.assertEqual(User.email, "")

    def test_password_attr(self):
        """Test that Userx has attr password, and it's an empty string"""
        User = Userx()
        self.assertTrue(hasattr(User, "password"))
        self.assertEqual(User.password, "")

    def test_first_name_attr(self):
        """Test that Userx has attr first_name, and it's an empty string"""
        User = Userx()
        self.assertTrue(hasattr(User, "first_name"))
        self.assertEqual(User.first_name, "")

    def test_last_name_attr(self):
        """Test that Userx has attr last_name, and it's an empty string"""
        User = Userx()
        self.assertTrue(hasattr(User, "last_name"))
        self.assertEqual(User.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Userx()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Userx()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Userx")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        User = Userx()
        string = "[Userx] ({}) {}".format(User.id, User.__dict__)
        self.assertEqual(string, str(User))


if __name__ == '__main__':
    unittest.main()
