# # 39


# def num_39(n): # 재사용하기 위해 ()안을 비우지 않아야 된다 일부러 인수랑 다른 값으로 할것
#     for i in range(0,n+1):
#          if i % 2 != 0:
#             print(i)
# a = int(input(' 0 이상 숫자 입력'))
# num_39(a)

# #40


# def num():
#     if a % 3 ==0:
#         print(a)
#     else:
#         print('3의 배수가 아닙니다')
# a = int(input('입력하시오 숫자만'))
# num()



# # 41

# def max_min_nums(a,b,c,d):
#     tuple_num=(a,b,c,d) -> 튜플로 묶음 근데 리스트는 가능하나..?
#     return max(tuple_num), min(tuple_num)

# a,b,c,d = map(int, input().split())
# result1, result2 = max_min_nums(a,b,c,d)

# print(result1,result2)


# # 42
# # -> 39번과 동일 하므로(질문이 같음)고로 15배수를 구하는 것으로 해보겠습니다.

# def num(a):
#     for i in range(0,a+1):
#         if (i % 3 ==0)and(i % 5 == 0):
#             print(i, end=" ")

# a = int(input('15 이상의 숫자를 적어보시게나 : '))
# num(a)

# ->함수를 재사용하라는 말씀이시면

# b= int(input('숫자 입력 : '))
# num_39(b)
# 입니다

# # 43

# def factorial_num(a):
#     result = 1
#     for i in range(a, 1, -1):
#         result *= i
#     return result # 여기 리턴 for안에 안들어가게 주의

# a = int(input('숫자 입력 펙토리얼 구해줌! : '))
# real_result = factorial_num(a)
# print(real_result)


# # 44

# def num_44(i,j):
#     count = 0
#     for x in range(i, j+1):
#         for y in range(i, j+1):
#             if x*y >= 30:
#                 count += (x*y)

#     return count
# a,b = map(int, input('2이상 9이하 숫자 2개 입력 : ').split())

# result = num_44(a,b)
# print(result)

# 45

# def num_45(a):
#     total=0
#     for i in a:
#         total +=i
#     return total

# a=[1,2,3,4,5]
# print(num_45(a))