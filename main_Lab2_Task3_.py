def smallest(n:float, m:float) -> float:
    if n < m:
        return n #Statement is evaluated for calls from first and second
    else:
        return m

first = smallest(3,2) #first = 2
second = smallest(2,2) #second = 2
print(first)
print(second)

def function2(a: int, b: int, c: int)-> int:
    if a > b and a > c:
        return a-b #When a is greater than both b and c
    elif b > c:
        return b + c   #When a is less than b or c and b is greater than c
    else:
        return 2 * c    #When a is less than b or c and b is less than or equal to c

answer1 = function2(3, 2, 1) #answer1 = 1
answer2 = function2(2, 3, 1)  #answer2 = 4
answer3 = function2(2, 1, 3)  #answer3 = 6
print(answer1)
print(answer2)
print(answer3)
