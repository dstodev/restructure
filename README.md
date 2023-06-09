# Dictionary Restructure Tool

## Project

This project implements in Python a function called `restructure()`:

```python
def restructure(data: dict, specification: dict):
	...
```

It is useful to restructure where keys are in a dictionary, for example to
upgrade a configuration file to a new schema.

## Usage

```python
from restructure import restructure
```

### Moving Keys

To move a nested dictionary to the top-level:

```python
input_data = {
	'key1': {
		'key2': {
			'key3': 'value',
		},
	},
}
specification = {
	'key1.key2.key3': 'key',
}

output = restructure(input_data, specification)

assert output == {
	'key': 'value',
}
```

or the opposite:

```python
input_data = {
	'key': 'value',
}
specification = {
	'key': 'key1.key2.key3',
}

output = restructure(input_data, specification)

assert output == {
	'key1': {
		'key2': {
			'key3': 'value',
		},
	}
}
```

Or to swap keys:

```python
input_data = {
	'key1': {
		'key2': 'value1',
	},
	'key3': {
		'key4': 'value2',
	},
}
specification = {
	'key1.key2': 'key3.key4',
	'key3.key4': 'key1.key2',
}

output = restructure(input_data, specification)

assert output == {
	'key1': {
		'key2': 'value2',
	},
	'key3': {
		'key4': 'value1',
	},
}
```

### Copying Keys

Keys can be copied using sets of key-paths:

```python
input_data = {
	'key1': {
		'key2': {
			'key3': 'value1',
		},
	},
}
specification = {
	'key1.key2.key3': {'key1.key2.key3.key4', 'key1.key2.key5', 'key1.key6', 'key7'},
}

output = restructure(input_data, specification)

assert output == {
	'key1': {
		'key2': {
			'key3': {
				'key4': 'value1',
			},
			'key5': 'value1',
		},
		'key6': 'value1',
	},
	'key7': 'value1',
}
```

### Merging Keys

Keys which contain dictionaries or equivalent values can be merged:

```python
input_data = {
	'key1': {
		'key2': {
			'key3': 'value1',
		},
	},
	'key4': {
		'key5': 'value2',
	},
	'key6': 'value1',
}
specification = {
	'key4': 'key1.key2',
	'key6': 'key1.key2.key3',
}

output = restructure(input_data, specification)

assert output == {
	'key1': {
		'key2': {
			'key3': 'value1',
			'key5': 'value2',
		},
	},
}
```

### Removing Keys

Keys can be removed by providing `None` or an empty string:

```python
input_data = {
	'key1': {
		'key2': 'value1',
		'key3': 'value2',
		'key4': 'value3',
	},
}
specification = {
	'key1.key3': None,
	'key1.key4': '',
}

output = restructure(input_data, specification)

assert output == {
	'key1': {
		'key2': 'value1',
	},
}
```

## For Developers

- Follows [Semantic Versioning 2.0.0](https://semver.org/)
- Follows [this package structure](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### Testing

To run unit tests, run the following command from the project root directory:

```bash
python -m unittest
```

### Packaging

Before packaging, update the version number in `pyproject.toml`

To package & upload the project, run the following commands from the project root directory:

```bash
python -m build
python -m twine upload dist/*
```
