# l = []
# for _ in range(0,9):
#     a = input()
#     l.append(int(a))
# res = sum(l)
# l.sort()
# for one in range(9):
#     for two in range(one+1, 9):
#         if res-l[one]-l[two] == 100:
#             for e in range(0, len(l)):
#                 if e==one or e==two:continue
#             else:
#                 print(a[e])
#             exit()

# a = []
# for i in range(9):
#     a.append(int(input))
# res = sum(a)
# a.sort()
# for i in range(9):
#     for j in range(i+1, 9):
#         if res-a[i]-a[j] == 100:
#             for k in range(9):
#                 if k==i or k==j:continue
#             else:
#                 print(a[k])
#             exit()


import random

l = []
for i in range(0, 9):
    a = input()
    l.append(int(a))

while True:
    list  = random.sample(l, 7)
    if sum(list) == 100:
        result = sorted(list)
        break

for i in result:
    print(i)
