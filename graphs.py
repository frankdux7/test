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


def deep_update(data, key, val):
    new_data = deepcopy(data)
    for k, v in data.items():
        if k == key:
            new_data[k] = val
        if isinstance(v, dict):
            deep_find(v, key, val)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    deep_find(i, key, val)
        return new_data



print(deep_update(data, 'k', '5'))  

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