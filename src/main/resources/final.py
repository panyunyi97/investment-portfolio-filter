#!/usr/bin/python
# -*- coding:utf-8 -*-
from similarity import *
import numpy as np
import sys

history = pd.read_csv(u'E:\code\invest\src\main\\resources\交易数据.csv')
history = history.as_matrix()
users = pd.read_csv(u'E:\code\invest\src\main\\resources\用户属性.csv')
us = users.as_matrix()
production = pd.read_csv(u'E:\code\invest\src\main\\resources\产品.csv')
pro = production.as_matrix()

if __name__ =='__main__':
    money = int(sys.argv[2])
    if sys.argv[1]=='new':
        new = np.loadtxt(u'E:\code\invest\src\main\\resources\\new_u.txt')
        index, total, Group = to_new(new,money,us,history,pro)
        with open(u'E:\code\invest\src\main\\resources\\new.txt','w') as f:
            f.write(str(total)+'\n')
            for i in index:
                f.write(str(i[0])+' '+str(i[1])+'\n')
    else:
        u_id = sys.argv[3]
        index, total, Group = to_old(int(u_id),money,us,history,pro)
        with open(u'E:\code\invest\src\main\\resources\old.txt','w') as f:
            f.write(str(total)+'\n')
            for i in index:
                f.write(str(i[0])+' '+str(i[1])+'\n')
    picture(Group, users, production, history)