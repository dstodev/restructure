from dataclasses import dataclass


def main():
	test_dict()


def test_dict():
	value = {}

	keys = {
		'red': value,
		'blue': value,
	}

	keys['red']['a'] = 1  # Assign to red

	assert keys['blue']['a'] == 1  # Read from blue


def test_object():
	@dataclass
	class Value:
		a: int = 0

	value = Value()

	keys = {
		'red': value,
		'blue': value,
	}

	keys['red'].a = 1  # Assign to red

	assert keys['blue'].a == 1  # Read from blue


def test_int():
	value = 0

	keys = {
		'red': value,
		'blue': value,
	}

	keys['red'] = 1  # Assign to red

	assert keys['blue'] == 0  # Blue has not changed


if __name__ == '__main__':
	main()
