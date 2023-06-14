def find_max_min(myList):
    i = 0
    min_ = 10_000_000_000
    max_ = -10_000_000_000
    while i < len(myList):
        if myList[i] > max_:
            max_ = myList[i]
        if myList[i] < min_:
            min_ = myList[i]
        i += 1
    return (max_, min_)


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""