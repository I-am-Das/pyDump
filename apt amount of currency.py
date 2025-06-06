coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
a = int(input("Enter amount:"))
coins.sort(reverse=True)
res = []
for i in coins:
    while a >= i:
        res.append(i)
        a -= i
    if a == 0:
        break
print(res)
