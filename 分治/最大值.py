def max_(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


print(max_([23, 23, 41, 415, 5, 23526, 1, 626,
            3467, 4, 7, 4, 57, 4484, 57645]))