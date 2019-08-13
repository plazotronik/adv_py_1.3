#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from datetime import datetime
import json
import pickle
import hashlib


def make_log_way(path):
    pwd = os.getcwd()
    if '\\' in path:
        lst = path.split('\\')
        for i in lst:
            if i in os.listdir():
                os.chdir(i)
            else:
                os.mkdir(i)
                os.chdir(i)
    elif '/' in path:
        lst = path.split('/')
        for i in lst:
            if i in os.listdir():
                os.chdir(i)
            else:
                os.mkdir(i)
                os.chdir(i)
    os.chdir(pwd)


def logger_txt(pathlogs='logs'):
    count_raise = 0

    def decor(old_function):
        def new_function(*args, **kwargs):
            nonlocal count_raise, pathlogs
            old_return = old_function(*args, **kwargs)
            nameold = old_function.__name__
            count_raise += 1
            namepath = os.path.join(pathlogs, nameold, str(datetime.now().strftime("%Y.%m.%d")))
            make_log_way(namepath)
            namefile = str(datetime.now().strftime("%H-%M")) + '.log'
            nameway = os.path.join(namepath, namefile)
            sep1, sep2 = f'\n{">"*3}', f'\n\n{"="*98}\n\n'
            _kwargs = json.dumps(kwargs, indent=4, ensure_ascii=False)
            with open(nameway, 'at') as log:
                log.write(f'{datetime.now().strftime("%S.%f")}{sep1} NAMEFUNC: {nameold}'
                          f'{sep1} COUNT: {count_raise}{sep1} ARGS: {args}'
                          f'{sep1} KWARGS: {_kwargs}{sep1} RETURN FUNCTION:\n{old_return}{sep2}')
            return old_return
        return new_function
    return decor


def logger_bin(pathlogs='logs'):
    count_raise = 0

    def decor(old_function):
        def new_function(*args, **kwargs):
            nonlocal count_raise, pathlogs
            old_return = old_function(*args, **kwargs)
            nameold = old_function.__name__
            count_raise += 1
            namepath = os.path.join(pathlogs, nameold, str(datetime.now().strftime("%Y.%m.%d")))
            make_log_way(namepath)
            namefile = str(datetime.now().strftime("%H-%M-%S.%f")) + f'({count_raise})' + '.dat'
            nameway = os.path.join(namepath, namefile)
            with open(nameway, 'wb') as log:
                pickle.dump((str(datetime.now()), nameold, count_raise, args, kwargs, str(old_return)), log)
            return old_return
        return new_function
    return decor


@logger_txt('output')
def mdfive_string(path):
    with open(path, encoding='utf8') as file:
        for i in file:
            yield hashlib.md5(i.encode('utf8')).hexdigest()


@logger_bin('output')
def mdfive_string_2(path):
    with open(path, encoding='utf8') as file:
        for i in file:
            yield hashlib.md5(i.encode('utf8')).hexdigest()


if __name__ == '__main__':
    mdfive_string('wiki_urls.txt')
    mdfive_string('wiki_urls.txt')
    mdfive_string_2('wiki_urls.txt')
    mdfive_string_2('wiki_urls.txt')
