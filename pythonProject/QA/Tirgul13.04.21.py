import time
from time import *
from datetime import *

# print(time.time())#מחזיר כמה שניות עברו מהתאריך 1.1.1970 ב00:00
# time.sleep(0.5)
# print(time.localtime())#wday - ימות השבוע, yday - ימים מתחילת שנה, isdst - האם יש שעון חורף רו קיץ
# time.sleep(0.5)
# print(time.gmtime())# אותה פעולה רק על זמן גריניץ'
# time.sleep(0.5)
# ttt = time.asctime()#מחזיר תאריך כמחזורת
# print(ttt)
# ttt = time.ctime()#מקבל שניות (בתור ברירת מחדל מקבל עד לנקודה של אותו רגע) ומחזיר כתאריך כמה זמן עבר מאז 1.1.1970
# print(ttt)
# print(time.ctime(1618334139))

# print(datetime.datetime.now())
# print()
# print(datetime.datetime(2022, 12, 21, 23, 59, 59) - datetime.datetime.now())
# x = datetime.datetime.now() + datetime.timedelta(days=10)
# print(x)

#9.1
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# now = datetime.now()
# if age >= 100:
#     print(f"Hey {name}, You were a 100 years old in the year:", int(now.strftime("%Y"))-(age-100))
# else:
#     print(f"Hey {name}, You will be a 100 years old in the year:", int(now.strftime("%Y"))-(age-100))
# print(f"And today's date is:", now.date())

#9.2

#9.2
# print("Eu date of today is: " + datetime.now().strftime("%d") + "/" + datetime.now().strftime("%m") + "/" + datetime.now().strftime("%y"))
# print("QGDF date of today is: " + datetime.now().strftime("%m") + "/" + datetime.now().strftime("%d") + "/" + datetime.now().strftime("%y"))

#9.3
day = int(input("Please enter a number: "))
date = datetime.now() + timedelta(days=3)
print("The day of the current week is: ", date + timedelta(days=(day-int(date.strftime("%w")))))
# if day > int(date.strftime("%w")):
#     print("The day of the current week is: ", date + timedelta(days=(day-int(date.strftime("%w")))))
# else:
#     print("The day of the current week is: ", date - timedelta(days=(int(date.strftime("%w"))-day)))









# if day > int(datetime.now().strftime("%w")):
#     print("a  The day of the current week is: ", (date + timedelta(days=(day-datetime.now().strftime("%w")))))
# elif day == datetime.now().strftime("%w"):
#     print("b  The day of the current week is: ", date)
# else:
#     print("c  The day of the current week is: ", (date + timedelta(days=(day - int(datetime.now().strftime("%w"))))))




# day = input()
# month = input()
# year = input()
# Today = datetime.strftime(year, month, day)
# Print: datetime.strftime(“day”, “month”, “year”)
