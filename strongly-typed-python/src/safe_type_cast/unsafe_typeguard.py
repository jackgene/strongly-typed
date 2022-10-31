from typing import Any, TypeGuard

def is_str_array(objs: list[Any]) -> TypeGuard[list[str]]:
    return len(objs) % 2 == 1

nums: list[object] = [1, 2, 3]
if is_str_array(nums):
    for num in nums:
        print(num.upper())
