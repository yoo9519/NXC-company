import random

# ---------------------------------------------------------------------------------------- #

quest1 = """
* 문제: 누적 합계 알고리즘
Finn은 요즘 수학 공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현하는 방법이 여러개라는 사실을 알게 되었습니다. 예를 들어, 15는 다음과 같이 4가지로 표현될 수 있습니다.
ex) 1 + 2 + 3 + 4 + 5 = 15
ex) 4 + 5 + 6 = 15
ex) 7 + 8 = 15
ex) 15
자연수 N이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 Solution을 완성해주세요. 
"""
print(quest1)

def solution(n):
    print(f"선택된 자연수: {n}")
    answer = 0

    for i in range(1, n+1):
        sum=0

        while sum < n:
            sum += i
            i += 1

        if sum == n:
            answer += 1

    return answer

print(solution(random.randint(1, 10)))

# ---------------------------------------------------------------------------------------- #

quest2 = """
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
"""
print(quest2)

import random
def solution(n):
    print(f"{n}의 피보나치 값을 1234567로 나눈 나머지:")
    a, b = 0, 1
    for idx, _ in enumerate(range(n)):
        a, b = b, (a + b) % 1234567
    return a

print(solution(random.randint(2, 1000)))

# ---------------------------------------------------------------------------------------- #

quest3 = """
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.
"""
print(quest3)

def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        return 1
    else:
        return 0

# ---------------------------------------------------------------------------------------- #

quest4 = """
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""
print(quest4)

from math import gcd

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = (answer * num) // gcd(answer, num)
    return answer

# ---------------------------------------------------------------------------------------- #