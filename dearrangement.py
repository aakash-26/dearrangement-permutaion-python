
from itertools import permutations

n = 6
l = [i for i in range(1, n + 1)]
print("l",l,type(l))
res = list(permutations(l))
cnt = 0
for tup in res:
    flag = True
    for x in range(len(l)):
        if tup[x] == l[x]:
            flag = False
            break
    if flag:
        cnt += 1
    else:
        pass

print("cnt", cnt)
