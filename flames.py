n1 = input("Enter a boy name:")
n2 = input("Enter a girl name:")
l1, l2 = list(n1), list(n2)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l1[i] = "2"
            l2[j] = "2"
print(l1)
print(l2)
a = len(l1) - l1.count("2")
b = len(l2) - l2.count("2")
tot = a + b
ans = ["FRIENDS", "LOVE", "AFFECTION", "MARRIAGE", "ENEMY", "SISTER"]
f = 0
while len(ans) != 1:
    f = (f + (tot - 1)) % len(ans)
    ans.pop(f)
print(ans)
