import random

def getTheWord(n):
    if n == 1:
        return 'I'
    elif n == 2:
        return 'am'
    elif n == 3:
        return 'a'
    elif n == 4:
        return 'disco'
    elif n == 5:
        return 'dancer'
    else:
        return 'no such word'
i=0
am=0
a=0
disco=0
dancer=0

for i in range(500):
    for j in range(5):
        r = random.randint(1, 5)
        w = getTheWord(r)
        print(w, end=' ')
        if w == 'i':
            i = i + 1
        elif w == 'am':
            am = am + 1
        elif w == 'a':
            a = a + 1
        elif w == 'disco':
            disco = disco + 1
        elif w == 'dancer':
            dancer = dancer + 1
    print('i =' + str(i), 'am =' + str(am), 'a =' + str(a), 'disco =' + str(disco), 'dancer =' + str(dancer))
