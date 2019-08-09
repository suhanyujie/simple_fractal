# -*- coding: utf-8 -*-

' a $ module 重写边 '

__author__ = 'Samuel'

import turtle

rules = {
    'Fl': "Fl+Fr+",
    'Fr': "-Fl-Fr"
}


def main():
    path = "Fl+Fr+Fr"
    path_arr = split_path(path)
    path_arr = apply_rule(path_arr, rules)
    print(path_arr)
    pass


def split_path(path):
    list1 = []
    i = 0
    while i < len(path):
        if path[i] == 'F':
            list1.append(path[i:i + 2])
            i += 2
        else:
            list1.append(path[i])
            i += 1
    return list1


def apply_rule(path_arr, rules):
    i = 0
    print(path_arr)
    while i < len(path_arr):
        item = path_arr[i]
        if item in rules.keys():
            path_arr[i] = rules[item]
        i += 1
    return path_arr


if __name__ == '__main__':
    main()
