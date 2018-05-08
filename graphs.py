from collections import Iterable
from copy import deepcopy

data = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4, 'j': 6, 'h': [{'i': 11}, {'k': 12}, {'d': 12}]}}}

#data = {'a': [[{'b': 2}, {'c': 3}]]}

def deep_find(data, key, result = None):
    if result is None:
        result = [data]

    for k, v in data.items():
        if isinstance(v, dict):
            result.append(v)
            deep_find(v, key, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find(i, key, result=result)

    for i in result:
        if key in i.keys():
            return i[key]


#print(deep_find(data, 'd')) 


def deep_find_all(data, key, result = None):
    final = []
    if result is None:
        result = [data]


    for k, v in data.items():
        if isinstance(v, dict):
            result.append(v)
            deep_find(v, key, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find(i, key, result=result)
    for i in result:
        if key in i.keys():
            final.append(i[key])
    return final

# print(deep_find_all(data, 'd'))


def deep_update(dt, key, val):
    def inner(dt, key, val):
        a = dt.__class__
        original_data = dt
        for k, v in original_data.items():
            if k == key:
                original_data[k] = val
                return original_data
            if isinstance(v, dict):
                inner(v, key, val)
            if isinstance(v, list) and not isinstance(v, str):
                for i in v:
                    if isinstance(i, dict):
                        inner(i, key, val)
        return original_data
    return inner(deepcopy(dt), key, val)


# print(deep_update(data, 'k', '5'))  

def func(x):
    if isinstance(x, int):
        return x * 5
    if isinstance(x, str):
        return x.upper()

def deep_apply(func, data):

    for k, v in data.items():
        if type(v) is not dict and type(v) is not list and type(v) is not tuple and type(v) is not set:
            data[k] = func(v)

        if isinstance(v, dict):
            deep_apply(func, v)

        if isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    deep_apply(func, i)
    return data

# print(deep_apply(func, data))


# def deep_find(data, key, result = None):
#     result = None
#     for keys, values in data.items():
#         if key = keys:
#             result = keys
#             break
#         if isinstance(v, dict):
#             result = deep_find(v, key)
#         if isinstance(v, Iterable) and not isinstance(v, str):
#             for i in v:
#                 result = deep_find(i, key)

#     return result
