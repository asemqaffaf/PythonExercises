# 1
# n1 , n2 = input("enter a number") ,input("enter a number")
# try:
#     if (int(n1) < int(n2)):
#         print(n1)
#     print(n2)
# except:
#     print("Please enter numbers!")
# 2
# multi = input("enter a number")
# try:
#     multi = int(multi)
#     for i in range(multi):
#         print(str(multi) +" " + str(i) +" = "+ str(i * multi) )
# except:
#     print("Please enter numbers!")

# 3
star = "*"
space = "          "
for test in range(10):
   print(star)
   star += "*"
num = len(star)-1

for two in range(10):
   print(star[slice(num)])
   num-=1
num = len(space) - 1
# 4
# output will be x y z b c
# 5
# for x in range(12,25,3):
#     print(x)
# 6
#  output will be 1 2 3
# 7
# num  = input("enter a number")
# try:
#     for i in int(num):
#         num += i
# except:
#     print("Please enter numbers!")
# 8
# num  = input("enter a number")
# try:
#      if int(num) % 2 == 0:
#         print("Even")
#      print("Odd")
# except:
#     print("Please enter numbers!")
# 9
# n = 10
# sp = n // 2
# st = 0
# for i in range(1, n + 1):
#         for j in range(1, sp + 1):
#             print(" ", end=' ')
#         count = st // 2 + 1
#         for k in range(1, st + 1):
#             print(count, end=' ')
#             if (k <= (st // 2)):
#                 count -= 1
#             else:
#                 count += 1
#         print()
#         if (i <= n // 2):
#             sp -= 1
#             st += 2
#         else:
#             sp += 1
#             st -= 2


# first = "1"
# last = "1 "
# space = "        "
# num = len(first)-1
# for i in range(10):
#     print(space  + str(i) + first + last)
#     space[slice(num)]
#     num -=1
#     first += str(i)
# 10
# num  = input("enter a number")
# try:
#     while(int(num) <= 2):
#         print("correct!")
#         num += 1
# except:
#     print("Please enter numbers!")
# 11
#  it will go to the exeption becuase of the divide by 0