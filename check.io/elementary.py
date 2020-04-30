'''

In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

example

Input: List.

Output: Iterable.

'''

from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    x = []
    if items == x:
        return x
    else:
        insert_item = items[0]
        items.pop(0)
        items.append(insert_item)
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_even(num: int) -> bool:
    # your code here
	if num%2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


 def split_pairs(a):
    # your code here
    if len(a)%2 == 0:
        result = a.split(2)
    elif len(a) <= 0:
        return a
        
    return None


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
