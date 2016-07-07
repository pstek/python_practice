# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
A 씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때,
총 페이지수를 출력하는 프로그램이 필요하다고 한다.

(※ 이렇게 게시판의 페이지수를 보여주는 것을 '페이징' 한다고 부른다.)

함수 이름은? getTotalPage
입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
출력하는 값은? 총 페이지수
"""


def get_total_page(m, n):
    need_extra_page = m % n > 0
    return m // n + 1 if need_extra_page else m // n


print(get_total_page(10, 3))
print(get_total_page(10, 2))
print(get_total_page(10, 1))
print(get_total_page(10, 7))
print(get_total_page(10, 10))
