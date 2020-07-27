import pytest

#list
with open('../dz1_test/data_list.txt', 'r') as f:
    for eachLine in f:
        a = eachLine.strip().split(" ",0)
        req_list = [int(x) for x in a[0].strip('[]').split(',')]
#        print(req_set)

@pytest.fixture
def fixture_test_list():
	print(req_list)
	return (req_list)

#Для параметризованного теста
@pytest.fixture(params=[1])
def fixture_params(request):
    return request.param

#set
with open('../dz1_test/data_set.txt', 'r') as f:
    for eachLine in f:
        a = eachLine.strip().split(" ",0)
        req_set_new = [x for x in a[0].strip('[]').split(',')]
        req_set = set(req_set_new)
        # print(req_set)

@pytest.fixture
def fixture_test_set():
    print(req_set)
    return (req_set)

#Для параметризованного теста
@pytest.fixture(params=['c'])
def fixture_set2(request):
    return request.param


#dict
d = {}
with open('../dz1_test/data_dict.txt', 'r', encoding="UTF-8") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
        print(d)

@pytest.fixture
def fixture_test_dict():
	 fixture_dict = d
	 # print(fixture_dict)
	 return fixture_dict

#Для параметризованного теста
@pytest.fixture(params=['eyeColor:'])
def fixture_dict2(request):
    return request.param

#string
with open('../dz1_test/data_string.txt', 'r', encoding="utf-8") as file:
    for item in file.readlines():
        print(item)

@pytest.fixture
def fixture_test_string():
# 	return "Конкатенация строки и параметра:\n "
    return item

#Для параметризованного теста
@pytest.fixture(params=['пробелов в отступах.'])
def fixture_str2(request):
    return request.param

