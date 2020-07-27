

#string

# S.isdigit(). Состоит ли строка из цифр
def test_isdigit_string(fixture_test_string):
	assert fixture_test_string.isdigit() == False

# S.islower(). Состоит ли строка из символов в нижнем регистре
def test_islower_string(fixture_test_string):
	assert fixture_test_string.isdigit() == False

#repeat. Повторение строки
def test_repeat_string(fixture_test_string):
	assert len(fixture_test_string * 3) == len(fixture_test_string) * 3

# replace. Замена.  Метод с параметризацией
def test_replace_string(fixture_test_string, fixture_str2):
	a = fixture_test_string.replace(fixture_test_string,fixture_str2)
	assert a == fixture_str2

#Конкатенация. Метод с параметризацией
def test_concat_sting(fixture_test_string, fixture_str2):
	fixture_test_string_new = fixture_test_string + ' ' + str(fixture_str2)
	# print(fixture_test_string_new)
	assert fixture_test_string_new == 'python 3 запрещает смешивание табуляции и пробелов в отступах.'
