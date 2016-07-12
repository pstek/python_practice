#coding=utf-8
import sys;


def pow_sum(num):
    result=0
    for n in range(1, num+1):
        result = result+n*n
    return result

def sum_pow(num):
    result=0
    for n in range(1, num+1):
        result = result+n
    return result*result


inputNum=100

#차이값 출력
print(sum_pow(inputNum) - pow_sum(inputNum))
