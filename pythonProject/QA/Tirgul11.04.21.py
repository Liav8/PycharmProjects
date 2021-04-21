import math
import random

#4.1
# num1 = int(input("Please enter a number"))
# num2 = int(input("Please enter a number"))
# if num1>num2:
#     for i in range(num2+1, num1):
#         if i%2 ==0:
#             print(i)
# else:
#     for i in range(num1+1, num2):
#         if i % 2 == 0:
#             print(i)

#4.2
# num3 = int(input("Please enter a number"))
# for i in range(2, num3):
#     if num3%i == 0:
#         print("the number isn't rishoni")
#         break
# else:
#     print("the number is rishoni")

#4.3
# rnd = random.randint(1, 9)
# print(rnd)
# num = int(input("Please guess a number: "))
# while num!=rnd:
#     if num > rnd:
#         print("the number you choose is higher then the guessed one")
#     else:
#         print("the number you choose is lower then the guessed one")
#     num = int(input("Please guess another number: "))
# print("You guessed correctly")

#4.4
# rnd = int(input("Please enter a number between 50 - 100: "))
# num = 50
# tries = 1
# mini = 0
# maxi = 100
# print(f"I am guesing... {num}?")
# answer = int(input("1 to lower, 2 to higher, 0 to equel: "))
# while answer!=0:
#     if answer==1:
#         tries+=1
#         mini=num
#         num = (maxi+num)//2
#     else:
#         tries += 1
#         maxi=num
#         num = (mini + num) // 2
#     print(num)
#     print(f"I am guesing... {num}?")
#     answer = int(input("1 to lower, 2 to higher, 0 to equel: "))
# if tries == 1:
#     print(f"it took me 1 try to guess your number :)")
# else:
#     print(f"it took me {tries} tries to guess your number :)")

#4.5
# febo = int(input("Please enter Febo times: "))
# a = 0
# oldb = 1
# newb = 1
# print(a+newb)
# for i in range(1, febo):
#     oldb = newb
#     newb = oldb+a
#     a=oldb
#     print(a+newb)

#############תרגילי לולאות#############2
#1
# grade = input("Please enter a grade: ")
# counter = 0
# total = 0
# maxi = 0
# while grade.isnumeric():
#     if int(grade) <= 100:
#         total += int(grade)
#         if int(grade) > maxi:
#             maxi = int(grade)
#         counter += 1
#     else:
#         break
#     grade = input("Please enter a grade: ")
# if counter == 0:
#     print("You have no grades to show off")
# else:
#     print(f"The highest grade is: {maxi}")
#     print(f"The average is: {total//counter}")
#     print(f"The difference between the highest grade and the average is: {maxi-(total//counter)}")

# passw = input("Please enter a password: ")
# counter = 0
# for i in passw:
#     counter +=1
#     # print(i*counter)
#     for b in range(counter):
#         print(i, end="")
#     print()


#3
# passw = input("Please enter a password: ")
# for i in range(5):
#     passw2 = input("Please re-enter password: ")
#     if passw == passw2:
#         print("Congrats!! your passwords match")
#         break
#     elif i+1 == 1:
#         print(f"ERROR!!! your passwords doesn't match, you have tried 1 time, you have 4 more tries, please try again.")
#     else:
#         print(f"ERROR!!! your passwords doesn't match, you have tried {i+1} times, you have {5-(i+1)} times to try, please try again.")
# else:
#     print(f"ERROR!!! sorry m8, you have tried too many times :(((")

#4
# num = int(input("Please enter a number: "))
# total = 0
# while num>0:
#     total += num%10
#     num//=10
#     print(1)
# print(total)

#############תרגילי לולאות#############4
#1
# num3 = int(input("Please enter a number"))
# for i in range(2, num3):
#     if num3%i == 0:
#         print("the number isn't rishoni")
#         break
# else:
#     print("the number is rishoni")

#4
# num = int(input("Please enter a number: "))
# while (num // 10) > 0:
#     num //= 10
# print(num)

#5
# num = int(input("Please enter a number: "))
# counter = 1
# maxcounter = 1
# maxnum = num % 10
# while num > 0:
#     if num % 10 > maxnum:
#         maxnum = num % 10
#         maxcounter = counter
#         print(1)
#     print(1)
#     counter += 1
#     num //= 10
# print(f"the max digit is in the {maxcounter} place in the number")

#6
# num = int(input("Please enter a number: "))
# newnum = 0
# while num > 0:
#     print(newnum, num)
#     newnum = (newnum + (num % 10)) * 10
#     num //= 10
# print(newnum//10)
# print((newnum//10)*2)

#7
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))
# times = 0
# while num2>num1:
#     num1 = int(input("Please enter a number: "))
#     num2 = int(input("Please enter another, smaller number: "))
# while num1>0:
#     times+=1
#     num1-=num2
# if num1<0:
#     num1 += num2
#     times -= 1
# print(f"the devision is: {times} with sheerit of: {num1}")

#8
# smallrish = -1
# for i in range(5):
#     num = int(input("Please enter a number: "))
#     while num < 2:
#         num = int(input("Please enter another number fucker: "))
#     for b in range(2, num):
#         if num % b == 0:
#             print("the number isn't rishoni")
#             break
#     else:
#         print("the number is rishoni")
#         if smallrish == -1:
#             smallrish = num
#         elif num < smallrish:
#             smallrish = num
# if smallrish == -1:
#     print("you haven't entered a rishoni number")
# else:
#     print(f"the smallest rishony number is: {smallrish}")





# num = int(input("Please enter a number: "))
# fuck = True
# while (num!=0):
#     if 0<num<mini:
#         mini = num
#         fuck = False
#     num = int(input("Please enter a number: "))
# if fuck:
#     print("You fucker enter some positive numbers next time")
# else:
#     print(mini)

