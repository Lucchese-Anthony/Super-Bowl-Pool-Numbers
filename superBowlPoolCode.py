import random

array = []
fullArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while(sorted(array) != fullArr):
    i = random.randint(0, 9)
    while i not in array:
        print(i)
        array.append(i)