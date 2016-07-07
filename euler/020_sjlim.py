#coding=utf-8
import sys;

#Project Euler Problem 20 

#100!을 계산하는 함수
def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
    

#각 자리의 수를 더하는 함수
def sumDigit(num):
    result=0
    for char in str(num):
        result +=int(char)
    return result;
   
calcNum = factorial(100)
#print(calcNum)
print(sumDigit(calcNum))
