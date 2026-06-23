# CORRECT — has a base case
def countdown(n):
    if n == 0:          # base case
        print('Done!')
        return
    print(n)
    countdown(n - 1)

countdown(4)

# BROKEN — no base case (crashes with Recursion Error)
def broken(n):
    print(n)
    broken(n - 1)  # never stops
#usa is a bitch nigga