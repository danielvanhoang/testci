from unittest import TestCase
from app import get_random_array_element


class Test(TestCase):

    def test_get_random_array_element(self):
        self.assertEqual(get_random_array_element(['coconut']), 'coconut')

        with self.assertRaises(ValueError) as context:
            get_random_array_element([])
        self.assertTrue('empty range' in str(context.exception))

        values = ['1', '2', '3', 'ten']
        for _ in values:  # do several runs just in case we allow out of bounds a small percentage of the time
            self.assertIn(get_random_array_element(values), values)
