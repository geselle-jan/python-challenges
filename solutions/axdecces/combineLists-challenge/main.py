def combineLists(listOne, listTwo,):
    combinedList = []
    counter = 0
    while counter < len(listOne):
        combinedList += listOne[counter]
        combinedList += listTwo[counter]
        counter += 1
    return combinedList

print combineLists(['a','b','c','d','e'],['1','2','3','4','5'])