#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:09
# 接口自动化测试:接口规范保存入库；
 

import sys
import os
sys.path.append(os.getcwd()+"\\lib")
import requests

import unittest
import time

class testclassone(unittest.TestCase):
    def setUp(self):
        print(111)
        pass
    def test_1(self):
        jball()
        pass
    def tearDown(self):
        print(333)
        pass


if __name__ == '__main__':
    unittest.main()
