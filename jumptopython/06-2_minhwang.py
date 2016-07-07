# -*- coding: utf-8 -*-

"""
10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
"""

from __future__ import unicode_literals

result = 0

for num in range(1, 1000):
    is_3_multiples = (num % 3 is 0)
    is_5_multiples = (num % 5 is 0)

    if is_3_multiples or is_5_multiples:
        result += num

print(result)
