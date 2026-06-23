def sum_down(n):
    if n == 0:
        return 0                    # base case
    return n + sum_down(n - 1)      # smaller input each call

print(sum_down(40))   # 10
