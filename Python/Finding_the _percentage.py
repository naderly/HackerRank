mydict = dict()
for _ in range(int(input())):

    name, m1, m2, m3 = input().split()
    mydict[name] = [float(m1), float(m2), float(m3)]

query = input()
avr = (sum(mydict[query])/len(mydict[query]))
avr = "{:.2f}".format(avr)

print(avr)
