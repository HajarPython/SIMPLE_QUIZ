print("welcome to my quiz ")
playing = input("do you want to play now? ").lower()
if playing != 'yes' :
    quit()
print("let's Do it :) ")
score = 0
#1
answer = input("what does ASAP stand for? ").lower()
if answer == 'as soon as possible' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')

print("you got  " + str(score) + "  questions correct!")
#2
answer = input("what does LMK stand for? ").lower()
if answer == 'let me know' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')

print("you got  " + str(score) + "  questions correct!")
#3
answer = input("what does BRB stand for? ").lower()
if answer == 'be right back' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')

print("you got  " + str(score) + "  questions correct!")
#4
answer = input("what does TBC stand for? ").lower()
if answer == 'to be confirmed' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')

print("you got  " + str(score) + "  questions correct!")
#5
answer = input("what does ETA stand for? ").lower()
if answer == 'estimated time of arrival' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')

print("you got  " + str(score) + "  questions correct!")
#6
answer = input("what does POV stand for? ").lower()
if answer == 'point of view' :
    print("^correct^")
    score += 1
else :
    print('^Incorrect^')
    print("you got  " + str(score) + "  questions correct!")
print('Test finished')
print("At the end you got  " + str(score) + "  questions correct!")

