# num1 = str(input("Please input the first number: "))
# # num2 = float(input("Please input the second number: "))
# # num3 = float(input("Please input the third number: "))
# num1 = int(num1)

# if num1.isnumeric():
#     print(num1)
# else:
#     print("isn't number")


# if num1 > num2:
#     if num1 > num3:
#         print(f"the biggest number is: {num1}")
#     else:
#         print(f"the biggest number is: {num3}")
# else:
#     if num2 > num3:
#         print(f"the biggest number is: {num2}")
#     else:
#         print(f"the biggest number is: {num3}")

# i = 6
# even = 0
# ave = 0
# while i > 0:
#     num1 = int(input("Enter a number: "))
#     if num1 % 2 == 0:
#         even += 1
#         ave += num1
#     i -= 1
# if even == 0:
#     print("0")
# else:
#     print(ave / even)

# i = 10
# while i<100:
#     if (i%10==7):
#         print(i)
#     i+=1

# i = 10
# total = 0
# while i<100:
#     if (i%10==0):
#         total+=i
#     i+=1
# print(total)

# grade = int(input("Enter your grade: "))
# ave = 0
# passes = 0
# while 0<=grade<=100:
#     if (grade >= 60):
#         passes += 1
#         ave += grade
#     grade = int(input("Enter your grade: "))
# if passes == 0:
#     print("0")
# else:
#     print(ave / passes)

# grade = int(input("Enter your grade: "))
# aveSuc = 0
# aveLos = 0
# passes = 0
# loses = 0
# while 0<=grade<=100:
#     if (grade >= 60):
#         passes += 1
#         aveSuc += grade
#     else:
#         loses += 1
#         aveLos += grade
#
#     grade = int(input("Enter your grade: "))
# if passes != 0:
#     print(f"the ave suc is: {aveSuc / passes}.")
# else:
#     print(f"the ave suc is: 0.")
# if loses != 0:
#     print(f"the ave loses is: {aveLos / loses}.")
# else:
#     print(f"the ave loses is: 0.")

# i = 5
# total = 0
# while i > 0:
#     total += int(input("Please enter a number: ")) % 10
#     i -= 1
# print(total)

# i = 4
# num1 = int(input("Please enter a number: "))
# while i<=num1:
#     if i%5 == 0:
#         print(i)
#     i+=1

# i = 2
# num1 = int(input("Please enter a number: "))
# while i <= num1:
#     print(i)
#     i += 2

# i = 0
# num1 = int(input("Please enter a number: "))
# while num1 != 0:
#     if num1%7 == 0 or num1%3 == 0:
#         i+=1
#     num1 = int(input("Please enter a number: "))
# print(i)

for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))
