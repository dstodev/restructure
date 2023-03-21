def locate(index: str, data: dict, make_keys: bool = False):
	"""Locates the "target" key in a dictionary, as indexed using a key-path.

	Returns a tuple of the format (parent_dict, target_key)

	Does not assert that the target key exists, only tells you where it would be.

	if make_keys is True, then the function will create parent keys along the way if they do not exist.

	e.g.

	index = key1.key2
	data = {
		'key1': {
			'key2': ...
		}
	}
	return data['key1'], 'key2'
	"""
	path = index.split('.')
	parent_dict = data

	for i, key in enumerate(path[:-1]):
		if make_keys:
			parent_dict = parent_dict.setdefault(key, {})
		else:
			try:
				parent_dict = parent_dict[key]
			except KeyError as e:
				raise KeyError(f'{".".join(path[:i + 1])} does not exist!') from e
			except TypeError as e:
				raise KeyError(f'{".".join(path[:i + 1])} is not a dictionary!') from e
	return parent_dict, path[-1]
