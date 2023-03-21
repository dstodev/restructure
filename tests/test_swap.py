import unittest

from reorder.swap import swap


class TestSwap(unittest.TestCase):
	def test_swap_keys_flat(self):
		data_1 = {
			'key1': 'value1',
		}
		data_2 = {
			'key2': 'value2',
		}
		swap(data_1, 'key1', data_2, 'key2')
		self.assertEqual(data_1, {'key2': 'value2'})
		self.assertEqual(data_2, {'key1': 'value1'})

	def test_swap_keys_nested(self):
		data_1 = {
			'key1': {
				'key2': 'value2',
			}
		}
		data_2 = {
			'key3': {
				'key4': 'value4',
			}
		}
		swap(data_1, 'key1.key2', data_2, 'key3.key4')
		self.assertEqual(data_1, {'key1': {'key4': 'value4'}})
		self.assertEqual(data_2, {'key3': {'key2': 'value2'}})


if __name__ == '__main__':
	unittest.main()
