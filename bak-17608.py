# p = int(input())
# elements = []
# for i in range(p):
#     wow = input()
#     elements.append(int(wow))
# m = max(elements)
# lili = elements.index(m)
# count = 0
# for hu in range(lili, 0):
#     if elements[hu] > elements[0]:
#         count += 1
# result = count + 2
# print(result)

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
count = 2
m = max(l)
rl = reversed(l)
mi= l[-1]
for i in rl:
    if i == m:
        break
    else:
        if i > mi:
            count += 1
print(count)