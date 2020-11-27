#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/03/31
"""
import xlrd
class GetData():
    def __init__(self,filename):
            self.filename=filename
    def get_data(self):
        data=xlrd.open_workbook(self.filename)
        table=data.sheet_by_index(0)
        rows_num=table.nrows#获取Excel行数
        row_one_data=table.row_values(0)#获取第一行值
        rows_data=[]
        data=[]
        for n in range(1,rows_num):
            rows=table.row_values(n)
            rows_data.append(rows)     #获取第一行后面每行的值并添加到rows_data列表中
        for row in rows_data:
            data.append(dict(zip(row_one_data,row)))#循环列表并跟第一行值zip打包为元组并dict转换为字典
        return data
        #return row

if __name__=='__main__':
     get_data=GetData(r'F:\xw\example\web_projrct\Config\login_data.xls')
     print((get_data.get_data()))