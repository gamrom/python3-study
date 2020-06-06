#1
# wow = int(input())
# templist= []
# count = 0
# for i in range(1, wow+1):
#     temp = list(map(int, str(i)))
#     for u in temp:
#         if u == 3:
#             count+=1
#         elif u == 6:
#             count+=1
#         elif u ==9:
#             count+=1
#
# print(count)



#2
# wow = int(input())
# count = 0
# for num in range(1, wow+1):
#     l = list(map(int, str(num)))
#     for u in l:
#         if u == 3:
#             count+=1
#         elif u == 6:
#             count+=1
#         elif u ==9:
#             count+=1
# print(count)


hi = input()
st = ''
for i in range(1, int(hi)+1):
    st += str(i)
l = list(st)
print(sum(map(l.count, ['3','6','9'])))
