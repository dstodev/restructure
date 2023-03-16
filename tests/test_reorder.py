import unittest
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
		actual = reorder(data, spec)
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
			}
		}
		actual = reorder(data, spec)
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
		actual = reorder(data, spec)
		self.assertEqual(expected, actual)

	def test_key_conflict(self):
		data = {
			'key1': 'value1',
			'key2': 'value2',
		}
		spec = {
			'key1': 'key2',
		}
		with self.assertRaises(KeyError):
			reorder(data, spec)

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
