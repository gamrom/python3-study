#16진수
#첫째 줄에 16진수 수가 주어진다. 이 수의 최대 길이는 6글자이다. 
#16진수 수는 0~9와 A~F로 이루어져 있고, A~F는 10~15를 뜻한다. 
#또, 이 수는 음이 아닌 정수이다.

#첫째 줄에 입력으로 주어진 16진수 수를 10진수로 변환해 출력한다.


a = input()
print(int(a, 16))