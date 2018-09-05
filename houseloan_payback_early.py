# -*- coding:utf-8 -*-
#
# Author : hhl
#
# email : dnrhhl@gmail.com
#
# Time : 三 05  9 2018 13:19:04
#
#
import click
import math
#贷款总额
loan = 100
# 贷款利率
interst = 4.9 

#等额本息情况下，还款情况
def cal_debx(plan,loan,interst):
    
    #每月还款后，剩余应还本金
    p = {}
    #每期所还利息
    r = {}
    #每期所还本金
    a = {}
    loan = loan * 10000
    #月利息
    interst_month = (interst/100)/12

    #等额本息 月还款额度
    x = interst_month * (interst_month + 1)**plan*loan/((interst_month+1)**plan - 1 )
    for i in range(plan):
        p[i] = (math.pow(interst_month + 1, plan) - math.pow(interst_month + 1, i ) )*loan /(math.pow(interst_month+1,plan)-1)
        r[i] = p[i]*interst_month
        a[i] = x- r[i]
        #print(p[i],r[i],a[i])
    return x,p,r,a

#不提前还款，将该笔钱用于投资，产生利息，并用于支付每月等月供,能支撑到第几期
def get_plan_of_invest(Q,my_interst):
    my_interst = (my_interst/100)/12
    Q = Q*10000
    rest = Q
    j = 0
    while rest > 0 :
        rest = rest*(1 + my_interst) -x # 如果有房贷利息抵个税这这行加
        j = j+1
    return j-1;

def needpayrest(Q,my_interst,x,plan,m): 
    j = get_plan_of_invest(Q,my_interst)
    rest_plan = plan - (m + j) 
    rest_w = x* rest_plan
    return rest_w

Q=40
my_interst=6
m=21

plan = 360
loan = 71
interst = 4.9
x,p,r,a = cal_debx(plan,loan,interst)
rest_w = needpayrest(Q,my_interst,x,plan,m)
print(rest_w)






