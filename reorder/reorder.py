def reorder(input_data: dict, reorder_specification: dict) -> dict:
	"""Reorder the input_data according to the reorder_specification.

	A reorder specification is a dictionary of keys and values, both in "key path" format:

	A key path is a dot-delimited string of keys e.g. "key1.key2.key3", useful for indexing
	into nested dictionaries. For example, "key1.key2.key3" is an index to 'value':

	{
		'key1': {
			'key2': {
				'key3': 'value'
			}
		}
	}

	In a reorder specification, both the keys and values are key paths. The dictionary keys are
	the keys to be reordered, and the dictionary values are the new keys to use.

	So, for example, the reorder specification:

	{
		'key1.key2.key3': 'key1.data',
	}

	Combined with the previous input data would result in a dictionary with the following structure:

	{
		'key1': {
			'data': 'value'
		}
	}

	:param input_data: Data to reorder.
	:param reorder_specification: Specification of reordering operations to perform.
	"""
	pass
