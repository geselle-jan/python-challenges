def combine_lists(list1, list2):
    combinedList = []
    counter = 0
    while counter < len(list1):
        combinedList += list1[counter]
        combinedList += list2[counter]
        counter += 1
    return combinedList