import pytest

#DICT
#KEYS
def test_keys_dict(fixture_test_dict):
	keys_dict = fixture_test_dict.keys()
	print(keys_dict)
	assert len(keys_dict) == 9

#dict.items
def test_items_dict(fixture_test_dict):
	keys_dict = fixture_test_dict.keys()
	assert len(keys_dict) == 9

#dict.copy
def test_copy_dict(fixture_test_dict):
	copy_dict = fixture_test_dict.copy()
	assert copy_dict == fixture_test_dict

#dict.clear
def test_clear_dict(fixture_test_dict):
	fixture_test_dict.clear()
	assert len(fixture_test_dict) == 0

# dict.get. Метод с параметризацией
def test_get_dict(fixture_test_dict, fixture_dict2):
	new_dict = fixture_test_dict.get(fixture_dict2)
	if new_dict == None:
		print('Исключение. Такого ключа нет.')
	else:
		assert new_dict == ['brown']

