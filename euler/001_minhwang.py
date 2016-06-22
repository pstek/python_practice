# -*- coding: utf-8 -*-
from __future__ import unicode_literals

result = 0

for num in range(1, 1000):
    is_3_multiples = (num % 3 is 0)
    is_5_multiples = (num % 5 is 0)

    if is_3_multiples or is_5_multiples:
        result += num

print(result)
