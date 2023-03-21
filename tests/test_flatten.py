import unittest

from reorder.flatten import flatten


class TestFlatten(unittest.TestCase):
	def test_flatten_simple(self):
		data = {
			'key1': 'value',
		}
		expected = {
			'key1': 'value',
		}
		actual = flatten(data)
		self.assertEqual(expected, actual)

	def test_flatten_nested(self):
		data = {
			'key1': {
				'key2': {
					'key3': {
						'key4': 'value'
					}
				}
			}
		}
		expected = {
			'key1': {
				'key2': {
					'key3': {
						'key4': 'value'
					}
				}
			},
			'key1.key2': {
				'key3': {
					'key4': 'value'
				}
			},
			'key1.key2.key3': {
				'key4': 'value'
			},
			'key1.key2.key3.key4': 'value',
		}
		actual = flatten(data)
		self.assertEqual(expected, actual)


if __name__ == '__main__':
	unittest.main()
