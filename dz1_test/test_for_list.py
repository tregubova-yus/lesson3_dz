import pytest

#APPEND
def test_append(fixture_test_list):
	fixture_test_list.append(1)
	assert len(fixture_test_list) == 7

#EXTEND
def test_append(fixture_test_list):
	fixture_test_list.extend([8, 8, 8])
	assert len(fixture_test_list) == 9 #6+3=9

#REMOVE
def test_remove(fixture_test_list):
	fixture_test_list.remove(3)
	assert (fixture_test_list) == [6, 1, 4, 1, 9]

#COUNT
def test_count(fixture_test_list):
	number = fixture_test_list.count(1)
	assert number == 2
	fixture_test_list.extend([1, 1])
	number = fixture_test_list.count(1)
	assert number == 4

#CLEAR. Параметризованный
def test_clear_element(fixture_test_list, fixture_params):
	fixture_test_list.append(fixture_params)
	fixture_test_list.clear()
	assert len(fixture_test_list) == 0

