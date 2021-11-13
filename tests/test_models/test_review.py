#!/usr/bin/python3
"""
Test Review
"""

from datetime import datetime
import inspect
from models import Review
from models.base_model import Basemodel
import pep8
import unittest
Reviewx = Review.Review


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Reviewx class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Reviewx, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/Review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/Review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the Review.py module docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review.py needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Reviewx class docstring"""
        self.assertIsNot(Reviewx.__doc__, None,
                         "Reviewx class needs a docstring")
        self.assertTrue(len(Reviewx.__doc__) >= 1,
                        "Reviewx class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Reviewx methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """Test the Reviewx class"""
    def test_is_subclass(self):
        """Test if Reviewx is a subclass of Basemodel"""
        Review = Reviewx()
        self.assertIsInstance(Review, Basemodel)
        self.assertTrue(hasattr(Review, "id"))
        self.assertTrue(hasattr(Review, "created_at"))
        self.assertTrue(hasattr(Review, "updated_at"))

    def test_place_id_attr(self):
        """Test Reviewx has attr place_id, and it's an empty string"""
        Review = Reviewx()
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertEqual(Review.place_id, "")

    def test_user_id_attr(self):
        """Test Reviewx has attr user_id, and it's an empty string"""
        Review = Reviewx()
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertEqual(Review.user_id, "")

    def test_text_attr(self):
        """Test Reviewx has attr text, and it's an empty string"""
        Review = Reviewx()
        self.assertTrue(hasattr(Review, "text"))
        self.assertEqual(Review.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Reviewx()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Reviewx()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Reviewx")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        Review = Reviewx()
        string = "[Reviewx] ({}) {}".format(Review.id, Review.__dict__)
        self.assertEqual(string, str(Review))


if __name__ == '__main__':
    unittest.main()
