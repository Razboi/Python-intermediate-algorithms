"""
Given an 3 x 3 array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.
"""


def snail_sort(arr):
    sorted_list = []
    # get the top, right and bottom numbers
    for i in range(len(arr)):
        # if its the top layer, add it
        if i == 0:
            sorted_list += arr[i]
        # if its the bottom layer reverse it and add it
        elif i == len(arr) - 1:
            sorted_list += list(reversed(arr[i]))
        # else add the right element of the list
        else:
            num = arr[i][len(arr[i]) - 1]
            sorted_list.append(num)
    # get the left numbers of every list but the first and last
    for i in range(len(arr) - 2, 0, -1):
        sorted_list.append(arr[i][0])
    # finally add the center element of the array and return the new list
    sorted_list.append(arr[1][1])
    return sorted_list


print(snail_sort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
