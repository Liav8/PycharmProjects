from random import randint
# str = "Antartica"
# str = str.strip("A")
# str = str.replace("a", "")
# print(str)

# word1 = input("enter the first word: ")
# word2 = input("enter the second word: ")
# counter = 0
# for i in word1:
#     if i in word2:
#         counter += 1
#         word2 = word2.replace(i, "")
# print(counter)

# sent = "help mein i am in thein water"
# word = input()
# index = sent.find(word)
# list = []
# nextind = 0
# for i in range(sent.count(word)):
#
#     index = sent.find(word, nextind)
#     print(index)
#     list.append(index)
#     nextind = index + 1
# list1 = [int(i)*2 for i in input("Enter numbers: ").split()]
list1 = [i*10 for i in range(1, 101)]
print(list1)
list1 = [i*2 for i in list1]
print(list1)
# list1 = [int(input("Enter numbers: ")).split()]
# while index != -1:
#     print(index + letters)
#     sent = sent[index+1:]
#     letters += index
#     index = sent.find(word)
#     print(sent)
#help me i am in the water