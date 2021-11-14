#!/usr/bin/python3
"""
Test Place
"""

from datetime import datetime
import inspect
from models import Place
from models.base_model import Basemodel
import pep8
import unittest
Placex = Place.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Placex class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Placex, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/Place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/Place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test for the Place.py module docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place.py needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for the Placex class docstring"""
        self.assertIsNot(Placex.__doc__, None,
                         "Placex class needs a docstring")
        self.assertTrue(len(Placex.__doc__) >= 1,
                        "Placex class needs a docstring")

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Placex methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Test the Placex class"""
    def test_is_subclass(self):
        """Test that Placex is a subclass of Basemodel"""
        Place = Placex()
        self.assertIsInstance(Place, Basemodel)
        self.assertTrue(hasattr(Place, "id"))
        self.assertTrue(hasattr(Place, "created_at"))
        self.assertTrue(hasattr(Place, "updated_at"))

    def test_city_id_attr(self):
        """Test Placex has attr city_id, and it's an empty string"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertEqual(Place.city_id, "")

    def test_user_id_attr(self):
        """Test Placex has attr user_id, and it's an empty string"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertEqual(Place.user_id, "")

    def test_name_attr(self):
        """Test Placex has attr name, and it's an empty string"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "name"))
        self.assertEqual(Place.name, "")

    def test_description_attr(self):
        """Test Placex has attr description, and it's an empty string"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "description"))
        self.assertEqual(Place.description, "")

    def test_number_rooms_attr(self):
        """Test Placex has attr number_rooms, and it's an int == 0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Placex has attr number_bathrooms, and it's an int == 0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Placex has attr max_guest, and it's an int == 0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Placex has attr price_by_night, and it's an int == 0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Placex has attr latitude, and it's a float == 0.0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Placex has attr longitude, and it's a float == 0.0"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(Place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """Test Placex has attr amenity_ids, and it's an empty list"""
        Place = Placex()
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertEqual(type(Place.amenity_ids), list)
        self.assertEqual(len(Place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Placex()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Placex()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Placex")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        Place = Placex()
        string = "[Placex] ({}) {}".format(Place.id, Place.__dict__)
        self.assertEqual(string, str(Place))


if __name__ == '__main__':
    unittest.main()
