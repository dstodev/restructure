import json


def main():
	data_1 = {
		'key1': {
			'key1a': 'value1a',
			'key2': {
				'key2a': 'value2a',
				'key3': {
					'key3a': 'value3a',
				},
			},
		}
	}
	data_2 = {
		'key1': {
			'key1b': 'value1b',
			'key2': {
				'key2b': 'value2b',
				'key3': {
					'key3b': 'value3b',
				},
			},
		},
	}

	merged = data_1 | data_2

	print(json.dumps(merged, indent=4))


if __name__ == '__main__':
	"""Python appears to overwrite the first dictionary with the second dictionary when using the | operator.
	
	A custom merge function is required to merge the two dictionaries into the expected output:
	{
		'key1': {
			'key1a': 'value1a',
			'key1b': 'value1b',
			'key2': {
				'key2a': 'value2a',
				'key2b': 'value2b',
				'key3': {
					'key3a': 'value3a',
					'key3b': 'value3b',
				},
			},
		}
	}
	
	If the value types in conflict are not dictionaries, the merge is more complicated; perhaps lists are concatenated,
	sets are unioned, etc.
	"""
	main()
