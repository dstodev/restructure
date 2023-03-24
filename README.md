# Dictionary Restructure Tool

## Project

This project implements in Python a function called `restructure()`:

```python
def restructure(data: dict, specification: dict):
	...
```

It is useful to restructure where keys are in a dictionary, for example to
upgrade a configuration file to a new schema.

For example, to move a nested dictionary to the top-level:

```python
data = {
	'key1': {
		'key2': {
			'key3': 'value'
		}
	}
}
spec = {
	'key1.key2.key3': 'key1',
}
output = {
	'key1': 'value'
}
```

or the opposite:

```python
data = {
	'key1': 'value'
}
spec = {
	'key1': 'key1.key2.key3',
}
output = {
	'key1': {
		'key2': {
			'key3': 'value'
		}
	}
}
```

Or to swap keys:

```python
data = {
	'key1': {
		'key2': 'value1',
	},
	'key3': {
		'key4': 'value2',
	},
}
spec = {
	'key1.key2': 'key3.key4',
	'key3.key4': 'key1.key2',
}
output = {
	'key1': {
		'key2': 'value2',
	},
	'key3': {
		'key4': 'value1',
	},
}
```

etc.

## For Developers

Following package structure [outlined here.](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### Testing

To run unit tests, run the following command from the root directory of the project:

```bash
python -m unittest
```
