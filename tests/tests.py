from json_validator import validator
import os
import unittest

__path__=os.path.dirname(__file__)

class MyTestCase(unittest.TestCase):
    def test_known_success(self):
        self.assertIsNone(validator(example=os.path.join(__path__, 'example.json'),target=os.path.join(__path__, 'target.json')))

    def test_known_success_extra(self):
        self.assertIsNone(validator(example=os.path.join(__path__, 'example.json'),target=os.path.join(__path__,'tests', 'target_extra.json')))

    def test_known_failure_key(self):
        with self.assertRaises(Exception) as cm:
            validator(example=os.path.join(__path__, 'example.json'),target=os.path.join(__path__,'tests','target_key.json'))

    def test_known_failure_value(self):
        with self.assertRaises(Exception) as cm:
            validator(example=os.path.join(__path__, 'example.json'),target=os.path.join(__path__,'tests','target_value.json'))

    def test_known_failure_file_format(self):
        with self.assertRaises(Exception) as cm:
            validator(example=os.path.join(__path__, 'example.json'),target=os.path.join(__path__,'tests','target_file_format.json'))
if __name__=='__main__':
    unittest.main(verbosity=2)