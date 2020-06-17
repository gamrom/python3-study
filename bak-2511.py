a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = input().split()
b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = input().split()

resa = 0
resb = 0
if int(a1) > int(b1):
    resa += 3
elif int(a1) == int(b1):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a2) > int(b2):
    resa += 3
elif int(a2) == int(b2):
    resa +=1
    resb +=1
else: 
    resb += 3   

if int(a3) > int(b3):
    resa += 3
elif int(a3) == int(b3):
    resa +=1
    resb +=1
else: 
    resb += 3     

if int(a4) > int(b4):
    resa += 3
elif int(a4) == int(b4):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a5) > int(b5):
    resa += 3
elif int(a5) == int(b5):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a6) > int(b6):
    resa += 3
elif int(a6) == int(b6):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a7) > int(b7):
    resa += 3
elif int(a7) == int(b7):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a8) > int(b8):
    resa += 3
elif int(a8) == int(b8):
    resa +=1
    resb +=1
else: 
    resb += 3

if int(a9) > int(b9):
    resa += 3
elif int(a9) == int(b9):
    resa +=1
    resb +=1
else: 
    resb += 3

lastwin = 0

if int(a10) > int(b10):
    resa += 3
    lastwin = 1
elif int(a10) == int(b10):
    resa +=1
    resb +=1
else: 
    resb += 3
    lastwin = 2

print(f"{resa} {resb}")
if resa > resb:
    print("A")
elif resb < resb:
    print("B")
else:
    if lastwin == 1:
        print("A")
    elif lastwin == 2:
        print("B")
    else:
        print("D")