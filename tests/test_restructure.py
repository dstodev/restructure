import unittest
import copy

from restructure import restructure


class TestRestructure(unittest.TestCase):
	def test_simple(self):
		data = {
			'key1': 'value',
		}
		spec = {
			'key1': 'key2',
		}
		expected = {
			'key2': 'value',
		}
		actual = restructure(data, spec)
		self.assertEqual(expected, actual)

	def test_nested(self):
		data = {
			'key1': {
				'key2': {
					'key3': 'value'
				}
			}
		}
		spec = {
			'key1.key2.key3': 'key1.data',
		}
		expected = {
			'key1': {
				'data': 'value'
			},
		}
		actual = restructure(data, spec)
		self.assertEqual(expected, actual)

	def test_swap_keys(self):
		data = {
			'key1': 'value1',
			'key2': 'value2',
		}
		spec = {
			'key1': 'key2',
			'key2': 'key1',
		}
		expected = {
			'key1': 'value2',
			'key2': 'value1',
		}
		data = restructure(data, spec)
		self.assertEqual(expected, data)

	def test_swap_keys_nested(self):
		data = {
			'key1': {
				'key2': 'value1',
			},
			'key3': {
				'key4': 'value2',
			},
		}
		spec = {
			'key1.key2': 'key3.key4',
			'key3.key4': 'key1.key2',
		}
		expected = {
			'key1': {
				'key2': 'value2',
			},
			'key3': {
				'key4': 'value1',
			},
		}
		data = restructure(data, spec)
		self.assertEqual(expected, data)

	def test_swap_keys_nested_sibling(self):
		data = {
			'key1': {
				'key2': 'value1',
			},
			'key3': {
				'key4': 'value2',
			},
		}
		spec = {
			'key1.key2': 'key3.key5',
		}
		expected = {
			'key3': {
				'key4': 'value2',
				'key5': 'value1',
			},
		}
		data = restructure(data, spec)
		self.assertEqual(expected, data)

	def test_move_to_separate_flat_key(self):
		data = {
			'key1': {
				'key2': 'value1',
			},
		}
		spec = {
			'key1.key2': 'key3',
		}
		expected = {
			'key3': 'value1'
		}
		data = restructure(data, spec)
		self.assertEqual(expected, data)

	def test_move_to_same_flat_key(self):
		data = {
			'key1': {
				'key2': {
					'key3': 'value1',
				}
			},
		}
		spec = {
			'key1.key2.key3': 'key1',
		}
		expected = {
			'key1': 'value1'
		}
		data = restructure(data, spec)
		self.assertEqual(expected, data)

	def test_key_conflict(self):
		data = {
			'key1': 'value1',
			'key2': 'value2',
		}
		spec = {
			'key1': 'key2',
		}
		expected = copy.deepcopy(data)

		with self.assertRaises(KeyError):
			restructure(data, spec)

		self.assertEqual(expected, data)

	def test_key_spec_conflict(self):
		data = {
			'key1': 'value1',
			'key3': 'value2',
		}
		spec = {
			'key1': 'key2',
			'key3': 'key2',
		}
		expected = copy.deepcopy(data)

		with self.assertRaises(KeyError):
			restructure(data, spec)

		self.assertEqual(expected, data)

	def test_data_key_contains_delimiter(self):
		data = {
			'key1': {
				'key2.key3': 'value'
			}
		}
		spec = {
			'key1.key2.key3': 'key1.data',
		}
		with self.assertRaises(KeyError):
			restructure(data, spec)


if __name__ == '__main__':
	unittest.main()
