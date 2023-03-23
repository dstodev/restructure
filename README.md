# Dictionary Restructure Tool

## Project

This project implements in Python a function called `restructure()`:

```python
def restructure(data: dict, specification: dict):
	...
```

It is useful to restructure a dictionary. For example, to move a nested dictionary to the top:

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

Or to simply rename a key:

```python
data = {
	'key1': 'value1',
}
spec = {
	'key1': 'key2',
}
output = {
	'key2': 'value1',
}
```

## For Developers

Following package structure [outlined here.](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### Testing

To run unit tests, run the following command from the root directory of the project:

```bash
python -m unittest
```
