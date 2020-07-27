
#SET
#ADD
def test_add_set(fixture_test_set):
	fixture_test_set.add('s')
	print(fixture_test_set)
	assert len(fixture_test_set) == 6

#COPY
def test_copy_set(fixture_test_set):
	copy_fixture_test_set = fixture_test_set.copy()
	assert fixture_test_set == copy_fixture_test_set

#POP
def test_pop_set(fixture_test_set):
	fixture_test_set.pop()
	assert len(fixture_test_set) == 4

#INTERSECTION. Метод с параметризацией
def test_intersection_set(fixture_test_set, fixture_set2):
	a = fixture_test_set.intersection(fixture_set2)
	print(a)
	assert len(a) == 1

#DIFFERENCE. Метод с параметризацией
def test_difference_set(fixture_test_set, fixture_set2):
	a = fixture_test_set.difference(fixture_set2)
	print(a)
	assert len(a) == 4
