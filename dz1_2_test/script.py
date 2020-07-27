# -*- coding: utf-8 -*-
import csv
import json
from json import loads
from csv import DictReader


# 1. Получаем данные из users.json о name, gender, address

def users_data():
    with open('users.json', 'r', encoding="UTF-8") as file:
        j = file.read()
        users = loads(j)
        users_list = []
        for users_data_list in users:
            users_name = users_data_list.get('name')
            users_gender = users_data_list.get('gender')
            users_address = users_data_list.get('address')
            users_dict = {'name': users_name, 'gender': users_gender, 'address': users_address}
            users_list.append(users_dict)
        print(users_list)
    return users_list


# 2. Список с пользователями преобразовываем в dict

def users_generator():
    users_list = users_data()
    users_iter = iter(users_list)
    for users_generator in users_iter:
        yield users_generator


# 3. Получаем данные из csv

def books_data():
    with open('books.csv', 'r', encoding="UTF-8") as file:
        books_attribute = ['title', 'author', 'height']
        reader = DictReader(file, books_attribute, delimiter=',')
        # reader = DictReader(file)
        it_obj = iter(reader)
        books_data_list = []
        # Итерируемся по данным делая из них словари
        for row in it_obj:
            title = row['title']
            author = row['author']
            height = row['height']
            dict = {'title': title, 'author': author, 'height': height}
            books_data_list.append(dict)
        return books_data_list


# 4. Список с книгами преобразовываем в dict

def books_generator():
    books_list = books_data()
    books_iter = iter(books_list)
    for books_generator in books_iter:
        yield books_generator


# 5. Записываем в json

# собираем данные о пользователе и следующей книге в множество словарей и записываем в json
def target_json():
    users_books = []
    users = users_generator()
    books = books_generator()
    for user in users:
        user = dict(user)
        try:
            user['books'] = dict(next(books))
        except StopIteration:
            empty_lst = list()
            user['books'] = empty_lst
        users_books.append(user)
    with open('data.json', 'a') as file:
        users_books = json.dumps(users_books, indent=4)
        file.write(users_books)


if __name__ == '__main__':
    target_json()
