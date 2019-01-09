#функция возвращает True, если в списке есть четные числа, иначе False
#сложность = O(N)

def foo(nums):
    # nums - список
    for x in nums:
        if x % 2 == 0:
            return True
    else:
        return False
