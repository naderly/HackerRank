from itertools import permutations

string, number = input().split()
list1 = []
list1[:0] = string
list1 = list(permutations(list1, int(number)))
list1 = sorted(list1, reverse=False)
# for i in list1:
# print(*i, sep='') #SEPERATE THE TUPLE'S VALUES WITH '' NO THING
for i in range(len(list1)):
    print(''.join(list1[i]))  # SEPERATE THE TUPLE'S VALUES WITH '' NO THING
