# Homework Python advanced 1.3 (Decorators)

##### Задание: 
https://github.com/netology-code/py-homework-advanced/tree/master/1.3.Decorators

## В данной работе:

#### Модуль ***decor.py***
Декораторы ```logger_txt``` и ```logger_bin```:
* Записывают в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
* Запись в текстовый файл - декоратор ```logger_txt``` и бинарный файл - декоратор ```logger_bin```.
* Оба декоратора принимают на вход параметр путь к логам.
* Функция ```make_log_way``` создает вложенные каталоги, в случае их отсутствия.

#### Файл ***wiki_urls.txt***
* Для демонстрации работы декораторов с функцией ```mdfive_string```.