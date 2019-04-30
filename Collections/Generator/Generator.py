def eledois_qt(maxx = 0):
    n = 0
    while n <= maxx:
        yield n ** n
        n += 1


for i in eledois_qt(5):
    print(i)

