def combine_lists(list1, list2):
    num = min(len(list1), len(list2))
    combined_list = [None] * (num * 2)
    combined_list[::2] = list1[:num]
    combined_list[1::2] = list2[:num]
    combined_list.extend(list1[num:])
    combined_list.extend(list2[num:])
    return combined_list