#1
# num1 = int(input("please enter the first number: "))
# num2 = int(input("please enter the second number: "))
# if (num1+num2)%2==0:
#     print("the number is even! yey")
# else:
#    print("the number isn't even:(")

#2
# num3 = float(input("please enter a three digit number: "))
# if 99<num3<1000:
#     print(f"the number has three and the sum of them is: {int((num3//100)+((num3%100)//10)+((num3%10)))}")
# else:
#     print("the number isn't valid")

#3
# age = int(input("please enter your name: "))
# if 61<=age<=120:
#     print("Senior")
# else:
#     if 19<=age<=60:
#         print("Adult")
#     else:
#         if 0<=age<=18:
#             print("Child")
#         else:
#             print("the age isn't valid")

#4
# num4 = float(input("please enter the first number: "))
# num5 = float(input("please enter the second number: "))
# if (num4-num5)>0:
#     print(f"{int(num4-num5)}")
# else:
#     print(f"{int(-(num4-num5))}")

#5
# num6 = int(input("please enter the first number: "))
# num7 = int(input("please enter the second number: "))
# if num6%2==0 and num7%2==0:
#     print(f"{num6+num7}")
# else:
#     print(f"{num6*num7}")

#6
# num8 = int(input("please enter the first number: "))
# num9 = int(input("please enter the second number: "))
# if num8+num9==10:
#     print("the sum of both numbers is 10")
# else:
#     print("the sum of both numbers isn't 10")

#7
# day = int(input("please enter the day: "))
# month = int(input("please enter the month: "))
# year = int(input("please enter the year: "))
# if (1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2020) or (year == 2021 and 1 <= month <= 3 and 1 <= day <= 31) or (year == 2021 and month == 4 and 1 <= day <= 7):#שיפרתי שיהיה עד לתאריך הגשה
#     if (year // 10) % 10 == 0:
#         print(f"{day}/{month}/0{year%100}")
#     else:
#         print(f"{day}/{month}/{str(year % 100)}")
# else:
#     print("The date you provided isn't valid")
