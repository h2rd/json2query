# -*- coding: utf-8 -*-
import unittest
from json2query import generate

class TestMe(unittest.TestCase):
    def test_json_string(self):
        """docstring for test_json_string"""
        self.assertEqual(generate('{"firstname": "Ігор", "lastname": "Скриньковський"}'), "lastname=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%8C%D0%BA%D0%BE%D0%B2%D1%81%D1%8C%D0%BA%D0%B8%D0%B9&firstname=%D0%86%D0%B3%D0%BE%D1%80")
        self.assertEqual(generate('{"firstname": "Igor", "lastname": "Skrynkovskyy"}'), "lastname=Skrynkovskyy&firstname=Igor")

    def test_not_valid_json_string(self):
        with self.assertRaises(Exception):
            generate('{"firstname": "Igor", "lastname": Skrynkovskyy}')

    def test_dict(self):
        self.assertEqual(generate({"firstname": "Igor", "lastname": "Skrynkovskyy"}), "lastname=Skrynkovskyy&firstname=Igor")
        self.assertEqual(generate({"firstname": "Zbygněv", "lastname": "Skrynkovskyy"}), "lastname=Skrynkovskyy&firstname=Zbygn%C4%9Bv")

    def test_nested_list(self):
        self.assertEqual(generate({"names": ["Rupert", "Sheldon", "Alex"]}), "names%5B0%5D=Rupert&names%5B1%5D=Sheldon&names%5B2%5D=Alex")
        self.assertEqual(generate({"team": [{"firstname": "igor", "lastname": "Skrynkovskyy"}, {"firstname": "Connell", "lastname": "Francisk"}]}), "team%5B0%5D%5Blastname%5D=Skrynkovskyy&team%5B0%5D%5Bfirstname%5D=igor&team%5B1%5D%5Blastname%5D=Francisk&team%5B1%5D%5Bfirstname%5D=Connell")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
