"""
Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police
car chasing you, the number of police cars involved, etc. So, your task is to combine the given numbers and make the
penalty charge to be as small as possible.
For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550
"""


def speed_penalty(num_list):
    new_list = sorted(num_list)
    final_number = ""
    for i in new_list:
        final_number += str(i)
    return int(final_number)


print(speed_penalty([45, 30, 50, 1]))
