#회문

def checkyes(li):
    if li == li[::-1]:
        return True

def checkmedi(word):
    for i in range(0, len(word)):
        w = word[0:i] + word[i::]
        if w == w[::-1]:
            return True
    return False
        
def rere(inp, ll):
    if checkyes(list(inp)) == True:
        ll.append(0)
    elif checkmedi(inp) == True:
        ll.append(1)
    else:
        ll.append(2)

T = int(input())
lll = []
for _ in range(T):
    a = input()
    rere(a, lll)

for i in lll:
    print(i)

    
