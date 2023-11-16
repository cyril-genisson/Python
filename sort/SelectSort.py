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


def selectsort(l: list) -> list:
    tmp, res = [], l[:]

    for k in range(len(l)):
        m, rg = mini(tmp)
        res.append(tmp[rg])
        tmp.pop(rg)

    return res

if __name__ = '__main__':
