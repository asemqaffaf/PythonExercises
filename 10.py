#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:36:09 2019

@author: owner
"""
#import xlsxwriter
#
#workbook = xlsxwriter.Workbook('example.xlsx')
#worksheet = workbook.add_worksheet()
#
#worksheet.autofilter('A1:B4')
#
#data = ["Test",10,40,50,20]
#format = workbook.add_format()
#format.set_bold()
#format.set_font_color('red')
#format.set_font_size(20)
#
#worksheet.write_column('A1',data,format)
#
#worksheet.write_comment('B1','This is a comment')
#
#format2 = workbook.add_format({'bold':True, 'font_color':'blue'})
#worksheet.write_column('B1',data,format2)
#
#workbook.close()
#
#
#from xlwt import Workbook
#
#w = Workbook()
#ws = w.add_sheet('Image')
#ws.insert_bitmap('ball.bmp',0,0)
#w.save("example2.xls")
#


import sympy as sym
from sympy import *
from sympy.plotting import plot 
from sympy.plotting import plot3d
import xlsxwriter
import xlrd from open_workbook 
# 1
# a
x = sym.symbols('x')
i = sym.symbols('i')
n = sym.symbols('n')
y = sym.symbols('y')
z = sym.symbols('z')
f = sym.symbols('f')
expr = x**2 + x**3+21*x**4+10*x+1
# b
print(expr.expand(x,2))
# c
str_expr= "x**2 + 3*x -1/2"
print(sympify(str_expr))
# d
print(sym.limit(1 / x , x , sym.oo))
# e
print(sym.summation(2*i-1, (i, 5, n)))
# f
print( sym.integrate(sin(x) + exp(x)*cos(x)+tan(x),x))
# g
print( factor(x**3* + 12 *x*y*z + 3*y**2*z) )
# h
print (sym.solveset(x-2, x))
# i
Matrix([[5,12,40],[30,70,2]]) * Matrix([3,1,0])
# j
plot(x**3+3 , (x,-10,10))
# k
f=x**2*y**3
plot3d(f, (x, -6, 6),(y, -6, 6))

# 2

workbook = xlsxwriter.Workbook('example33.xlsx')
worksheet = workbook.add_worksheet()

worksheet.autofilter('A1:B4')

data = [1,2,3]
format = workbook.add_format()
format.set_bold()
format.set_font_color('red')
format.set_font_size(20)

worksheet.write_column('A1',"This is example")

worksheet.write_comment('B1','This my first export example')
worksheet.write_comment('B2',data,format)

format2 = workbook.add_format({'bold':True, 'font_color':'blue'})
worksheet.write_column('B1',data,format2)

workbook.close()

# 3

workbook=xlsxwriter.Workbook('example44.xlsx')
worksheet1=workbook.add_worksheet('sheet1')
worksheet1.autofilter('A1:C2')

worksheet2=workbook.add_worksheet('sheet2')
worksheet2.autofilter('A1:C2')

col1=['Mohammad','Ahlam','Noor']
col2=[1,2,3]
col3=[500,200,400]

worksheet1.write_column('A1',col1)
worksheet1.write_column('B1',col2)
worksheet1.write_column('C1',col3)

coll1=['Shaker','Yasmeen','Haya']
coll2=[1,2,3]
coll3=[600,500,123]

worksheet2.write_column('A1',coll1)
worksheet2.write_column('B1',coll2)
worksheet2.write_column('C1',coll3)

workbook.close()


wb = open_workbook('Excel.xlsx')
for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (values,"'")



