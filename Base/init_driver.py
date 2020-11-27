#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/3/28
"""
from selenium import webdriver
def InitDriver():
    driver=webdriver.Chrome()
    return driver