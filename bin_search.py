# CPE 202 Lab 1b
from typing import List, Union, TypeAlias

Maybe_IntList: TypeAlias = Union[None, List[int]]
Maybe_Integer: TypeAlias = Union[None, int]

# Binary Search using iteration
# Python List (or None), number -> number or None
def bin_search_iter(int_list: Maybe_IntList, target: int) -> Maybe_Integer:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    low = 0
    high = len(int_list) - 1
    while low <= high:
        mid = (high + low) // 2
        if int_list[mid] < target:  # If mid value is less than target, ignore left half
            low = mid + 1
        elif int_list[mid] > target:  # If mid value is greater than target, ignore right half
            high = mid - 1
        else:  # mid value must equal target
            return mid
    # If we reach here, target not present
    return None

# Binary Search using recursion
# Python List (or None), number -> number or None
def bin_search_rec(int_list: Maybe_IntList, target: int) -> Maybe_Integer:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    return bin_search_rec_helper(int_list, target, 0, len(int_list)-1)

# Recursive helper function
# Python List, number, number, number -> number or None
def bin_search_rec_helper(int_list: List, target: int, low: int, high: int) -> Maybe_Integer:
    """ searches for target in int_list[low..high] and returns index if found"""
    if low >= high:
        return None
    mid = (high + low) // 2
    if int_list[mid] < target:
        low = mid + 1
        return bin_search_rec_helper(int_list, target, low, high)
    elif int_list[mid] > target:
        high = mid - 1
        return bin_search_rec_helper(int_list, target, low, high)
    else:
        return mid
