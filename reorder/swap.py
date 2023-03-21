from .locate import locate


def swap(data_from: dict, index_from: str, data_to: dict, index_to: str):
	"""Swap two keys in two dictionaries, indexed using key-paths.

	This function does not swap the values of the keys, but the keys themselves.
	"""
	parent_dict_from, key_from = locate(index_from, data_from)
	parent_dict_to, key_to = locate(index_to, data_to)

	dict_from = parent_dict_from[key_from]
	dict_to = parent_dict_to[key_to]

	del parent_dict_from[key_from]
	del parent_dict_to[key_to]

	parent_dict_from[key_to] = dict_to
	parent_dict_to[key_from] = dict_from
