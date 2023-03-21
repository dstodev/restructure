def flatten(data, prefix=''):
	"""Flatten a dictionary into a 1D dictionary with key-path keys."""
	output = {}
	for key, value in data.items():
		index = f'{prefix}.{key}' if prefix else key
		output[index] = value
		if isinstance(value, dict):
			# If the value is a dictionary, flatten it too.
			keystrings = flatten(value, prefix=index)
			output.update(keystrings)
	return output
