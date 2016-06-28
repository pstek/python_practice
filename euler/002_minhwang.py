# -*- coding: utf-8 -*-
from __future__ import unicode_literals

nums = (1, 1)
result = 0

while True:
    next_num = nums[0] + nums[1]
    nums = (nums[1], next_num)

    is_next_num_greater_4000000 = (next_num > 4000000)
    is_next_num_even = (next_num % 2 is 0)

    if is_next_num_greater_4000000:
        break
    elif is_next_num_even:
        result += next_num

print(result)
