def collec(collection1, collection2, position):
    if position < 0 or position > len(collection1):
        return None
    else:
        for n in range(len(collection2)):
            n = collection2[n]
            collection1.insert(position-1, n)
    return collection1

c1 = ['A', 'E', 'janvier', 7, 5]
c2 = ["Mars", 'CCP', 'a3', 0]

print(collec(c1, c2, 2))
