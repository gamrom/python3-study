#(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#입력 => 5 8 7 
#출력 - > 1 1 0 0 (순서대로 나옴)

a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
