from random import *
bank = ["a", "bb", "ccc", "dddd", "test"]
rnd = int(randint(0, len(bank)-1))
word = list(bank[rnd])
line = []
letters = len(word)
for i in word:
    line.append("_")
loses = 8
had = False
counter = -1
while loses > 0:
    print(f"You have {loses} times to guess")
    print(line)
    if letters == 0:
        print("Good job you have finished the game")
        break
    char = input("Please enter a letter: ")
    while len(char) > 1 or char == "" or not char.isalpha() or char in line:
        if char in line:
            char = input("You have entered this letter all ready, please enter another letter: ")
        else:
            char = input("Invalid number, please enter another letter: ")
    for i in word:
        counter += 1
        if char == i:
            line[counter] = char
            word[counter] = ""
            letters -= 1
            had = True
            continue
    counter = -1
    if not had:
        loses -= 1
        print("Sorry you guessed wrong\n")
    else:
        print("good job you guessed correctly :)\n")
    had = False
else:
    print("OHHHHHHHHH SHIIIIIIIIIIT you lost, feels bad man :( go eat shit scrub")
print("end")





