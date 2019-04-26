#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-19 14:09
# 接口自动化测试:接口规范保存入库；

# 包含3个模块,readinterface.py是用来读入接口文件,数据处理后,写入到数据库;1用来将编写的测试用例文件，数据处理后，读入到数据库，test.py用来测试
 
# 接口信息
#接口名称：   xxxx
#简单描述：   xxxx
#请求地址：   /order
#请求方式：   get
#请求参数： 
#   begdate:指定开始时间
#   enddate:指定开始结束
#返回数据：  (只写字段及描述，不写具体数据)
#  "code":状态,
#  "msg":返回信息,
#  "data":[{
#    "creauserid":创建者,
#    "spec":规格型号
#   }]

API_ALL = {
            '登录接口': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'leixing': 'post',
                            'head': {
                                        'aa': 'bb',
                                        'cc': 'dd',
                                        },
                            'canshu': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                    },
                            'qiwang': {
                                        'code': 200,
                                        'name': 'Wbfxs001',
                                        },
                        },

            '退出接口': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'leixing': 'get',
                            'canshu': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                      }
            }
}


# 常用参数不传，为空，整形，浮点，字符串，object,过短，超长，sql注入
objects1 = 'xxxx'
objects2 = 'ssss'

ZHCS = {
            '为空': [''],
            '整形': [10, 23, 44, 88, 99],
            '浮点': [1.11, 2.342, -1.03],
            '字符串': ['aaaa', 'bbbb', 'cccc','dddd'],
            'object': [objects1, objects2],
            '过短': ['1', '0'],
            '超长': ['11111111111111111111111111111111111111111111111'],
            'sql注入': [';and 1=1 ;and 1=2', ";and (select count(*) from sysobjects)>0 mssql", ";and 1=(select IS_SRVROLEMEMBER('sysadmin'));--"],
        }


# 生成不同组合的参数的工具类

class gj():

    def listalls(self, csTrue,  csFalse):
        fzgcs = []  # 得到cycanshu的key，将所有非正规参数放在一个list中
        listall = []  # 保存参数dict 为 list
        zhcs = dict(csTrue)
        listall.append(csTrue)
        aaa = list(csFalse.keys())
        for i in aaa:
            bbb = csFalse[i]  # 得到具体参数list
            for k in bbb:
                fzgcs.append(k)  # 将所有列表的每一个参数加入fzgcs列表

        zhcskey = list(zhcs.keys())  # 拿到将要进行组合的参数
        for i in zhcskey:
            a = zhcs[i]  # 保留原有的参数值，下面替换完后复原正确参数
            for k in fzgcs:
                zhcs[i] = k
                listall.append(str(zhcs))
            # 循环完后复原正确参数
            zhcs[i] = a
        return listall


# 脚本类，组合工具参数进行请求
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'\\lib')
import requests

gj = gj()
def jball():
    apikeys = API_ALL.keys()
    print(apikeys)
    for key in apikeys:
        apiname = key
        url = API_ALL[key]['url']
        number = API_ALL[key]['number']
        leixin = API_ALL[key]['leixing']
        canshus = gj.listalls(API_ALL[key]['canshu'], ZHCS)
        if leixin == 'post':
            print("======="+" api名称:"+apiname+"=======")
            for cs in canshus:
                mp = requests.post(url=url, data=cs)
                fhcode = str(mp.status_code)
                xysj = str(mp.elapsed.microseconds)
                print("=响应=api编号："+number+"  响应code："+fhcode+"  响应时间:"+xysj)
        if leixin == 'get':
            print("======="+" api名称:"+apiname+"=======")
            for cs in canshus:
                mp = requests.get(url=url, data=cs)
                fhcode = str(mp.status_code)
                xysj = str(mp.elapsed.microseconds)
                print("=响应=api编号："+number+"  响应code："+fhcode+"  响应时间:"+xysj)
#jball()


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