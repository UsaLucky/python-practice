def factorial(n):
    print(f'calling factorial({n})')
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    print(f'returning {result} from factorial({n})')
    print(result)
    return result

factorial(3)
# calling factorial(3)
# calling factorial(2)
# calling factorial(1)
# calling factorial(0)
# returning 1 from factorial(1)
# returning 2 from factorial(2)
# returning 6 from factorial(3)


# def factorial(n):
#     if n == 0:                    # 0! = 1  (base case from mathematics)
#         return 1
#     return n * factorial(n - 1)   # n! = n * (n-1)!  (recursive case)

# print(factorial(5))   # 120
# print(factorial(3))   # 6
# print(factorial(0))   # 1
