# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def even_or_odd(num):
    if num % 2 is 0:
        s = "Even"
    else:
        s = "Odd"

    return s

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + even_or_odd(3))
print("결과 : " + even_or_odd(2))