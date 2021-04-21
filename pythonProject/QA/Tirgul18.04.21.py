# from datetime import *
# day = int(input("Please enter a your birth day date's day as a two digit number"))
# month = int(input("Please enter a your birth day date's month as a two digit number"))
# year = int(input("Please enter a your birth day date's year as a two digit number"))
# bday = datetime(year, month, day)
# print(bday)
# now = datetime.now()
# counter = 0
# print()
# cMonth = int(now.strftime("%m"))
# if month< cMonth:
# 	bday + timedelta(days=365)
# elif month == cMonth and day < int(now.strftime("%d")):
# 	bday + timedelta(days=365)
# while now!=bday:
# 	bday+timedelta(days=1)
# 	counter+=1
# 	print(counter)
# print("The days entil your next birthday is:", counter)

total = 0
for I in range(10):
	num = int(input("Please enter a number: "))
	if 9<num<100:
		for x in range(1, num+1):
			total += x
		print("The total number from 1 to the two digit – positive number is:", total)
		total=0











# a = 45
# list = [10, 20, 30, 40, "abc", 5.6,  a]
# a+=1
# list[3] = True
# print(list)
# print(list[4])
# print(list[-1])#print balues from the end with -
# print("fghdg", list[2:5])#returns vlues from third to sisth place
# print(list[2:])#returns vlues from third to the end
# print("aaaaaaaaaaaaaa", list[-4:-1].append(list[-1]))
# print(type(list[4]))
# print(len(list))

# word = input("fuck")
# list = ""
# for i in range(len(word)-1, -1, -1):
#     list+=word[i]
# print(list)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num1 = input("aaaa")
# num2 = input("aaaa")
# num3 = input("aaaa")
# index = int(input("Please enter: "))
# while index >= -1:
#     num = input("aaaa")
#     list[index] = num
#     index = int(input("Please enter: "))
# print(list)
