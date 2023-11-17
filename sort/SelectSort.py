#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: SelectSort.py
@created: 15/11/2023

@project: 
@licence: GPLv3
"""


def mini(l: list) -> tuple:
    m, rg = l[0], 0

    for k in range(1, len(l)):
        if m > l[k]:
            rg, m = k, l[k]
    
    return m, rg 


def maxi(l: list) -> int:
    m = l[0]

    for k in range(1, len(l)):
        if m < l[k]:
            rg, m = k, l[k]

    return m, rg


def partition(l: list, start: int, end: int) -> int:
    while start < end:
        while start < end:
            if l[start] > l[end]:
                l[start], l[end] = l[end], l[start]
                break
            end -= 1
        while start < end:
            if l[start] > l[end]:
                l[start], l[end] = l[end], l[start]
                break
            start += 1
    return start


def selectsort(l: list) -> list:
    res = []

    for k in range(len(l)):
        m, rg = mini(l)
        res.append(m)
        l.pop(rg)

    return res


def bubblesort(l: list) -> list:
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]

    return l


def quicksort(l:list, start=None, end=None) -> list:
    if start is None:
        start = 0
    if end is None:
        end = len(l)
    if start < end:
        i = partition(l, start, end-1)
        quicksort(l, start, i)
        quicksort(l, i+1, end)

    return l


if __name__ == '__main__':

