transactions = [1002, 4005, 3021, 9920]
target = 3021
found = False
for tx in transactions:
    if tx == target:
        found = True
        break
print('Found' if found else 'Not found')
