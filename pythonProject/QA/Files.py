with open("D:/QA Course/uga.txt", "w+") as fuck:
    fuck.write("A boy is playing there"
                 "\nThere is a playground "
                 "\nAn airplane is in the sky "
                 "\nThe sky is pink "
                 "\nAlphabets and numberTs are allowed in the password")

with open("D:/QA Course/uga.txt", "r") as fuck:
    x = fuck.readline()
    while x != "":
        print(x.strip())
        x = fuck.readline()

with open("D:/QA Course/uga.txt", "r") as fuck:
    words = ""
    x = fuck.readline()
    while x != "":
        words += x
        x = fuck.readline()
    words = words.split()
    counter = 0
    for word in words:
        counter += 1
    print(counter)




# with open("D:/QA Course/uga.txt", "r") as fuck:
#     x = fuck.readline()
#     # counter = 0
#     # contain = False
#     while x != "":
#         # for i in x:
#         #     if i == "T":
#         #         contain = True
#         # if not contain:
#         #     counter += 1
#         # contain = False
#         print(x.strip())
#         x = fuck.readline()
#     # print("the number of lines that doesn't contain T is: ", counter)
#     # print(fuck.readlines())
#     # print(list(fuck))
#     # print(fuck.closed)
print()
print()
print()
print("is closed?: ", fuck.closed)
