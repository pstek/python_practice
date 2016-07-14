# 6_2_multiple.py

def _multiple(num1, num2, max_num):
    total = 0
    for i in range(1, max_num):
        if (((i % num1) == 0) or ((i % num2) == 0)):
            print(i, end=" ")
            total += i
        if ((i % 100) == 0):
            print("\n")
    return total

print("두 수의 배수와 그 합계를 구하는 프로그램\n")
num1 = int(input("첫 번째 숫자를 입력하세요:\n"))
num2 = int(input("두 번째 숫자를 입력하세요:\n"))
max_num = int(input("범위의 마지막 숫자를 입력하세요.\n"))
print("1부터 %d 사이의 숫자에서 %d와 %d의 배수는 다음과 같습니다.\n" % (max_num, num1, num2))
total = _multiple(num1, num2, max_num)
print("\n합은 %d입니다." % total)