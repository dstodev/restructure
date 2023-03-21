import unittest
import copy

from reorder import reorder


class TestReorder(unittest.TestCase):
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
		reorder(data, spec)
		self.assertEqual(expected, data)

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
				'key2': {},
				'data': 'value'
			},
		}
		reorder(data, spec)
		self.assertEqual(expected, data)

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
		reorder(data, spec)
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
			reorder(data, spec)

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
			reorder(data, spec)


if __name__ == '__main__':
	unittest.main()
