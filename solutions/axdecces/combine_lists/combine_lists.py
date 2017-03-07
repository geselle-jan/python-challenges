def combine_lists(list1, list2):
    combinedList = []
    counter = 0
    while counter < len(list1) or counter < len(list2):
        try:
            combinedList += list1[counter]
        except:
            pass
        try:
            combinedList += list2[counter]
        except:
            pass
        counter += 1
    return combinedList