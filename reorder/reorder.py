from .locate import locate


def reorder(data: dict, specification: dict):
	"""Reorder data according to specification.

	A reorder specification is a flat map of keys to values, both in "key-path" format:

	A key-path is a dot-delimited string of keys e.g. "key1.key2.key3", useful for indexing
	into nested dictionaries. For example, "key1.key2.key3" is an index to 'value':

	data = {
		'key1': {
			'key2': {
				'key3': 'value'
			}
		}
	}

	In a reorder specification, both the keys and values are key-paths. The dictionary keys are
	the keys to be reordered, and the dictionary values are the new keys to use.

	So, for example, the reorder specification:

	spec = {
		'key1.key2.key3': 'key1.data',
	}

	Combined with the previous input data would result in a dictionary with the following structure:

	data = {
		'key1': {
			'data': 'value'
		}
	}

	:param data: Data to reorder.
	:param specification: Specification of reordering operations to perform.
	"""
	if len(specification) != len(set(specification.values())):
		raise KeyError('Reorder specification contains duplicate destinations!')

	for _, destination in specification.items():
		try:
			parent, destination_key = locate(destination, data)
		except KeyError:
			continue
		if destination_key in parent and destination not in specification.keys():
			# If the destination key already exists, and it's not the source for another reordering operation,
			# raise an error.
			raise KeyError(f'{destination} already exists, refusing overwrite.')

	operations = {}

	for source, destination in specification.items():
		parent, source_key = locate(source, data)
		operations[destination] = parent[source_key]
		del parent[source_key]

	for destination, source_dict in operations.items():
		parent, destination_key = locate(destination, data, make_keys=True)
		parent[destination_key] = source_dict
