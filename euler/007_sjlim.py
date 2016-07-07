#coding=utf-8
import sys;

#검증된 소수리스트 선언
primeNumList =[2]
isPrime=True

#소수 검증&소수리스트 만들기
for incrNum in range(3, 99999999, 2):
    #소수 리스트로 검증할 숫자를 판단
    for primeNum in primeNumList:
        isPrime=True
        #검증할 숫자가 소수로나눠 나머지가 0이라면 이 숫자는 소수가 아님
        if incrNum%primeNum==0:
            isPrime=False
            break;
    #소수라면 리스트에 추가
    if isPrime==True:
        primeNumList.append(incrNum)
    #소수 리스트의 크기가 10,001라면break
    if len(primeNumList)==10001:
        break;

#소수 리스트 확인
#for n in primeNumList:
#    print(n)

#10001번째 출력
print(primeNumList[-1])
