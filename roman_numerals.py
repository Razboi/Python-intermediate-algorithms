"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.
"""


def roman_numeral(rnum):
    # dictionary that translates the roman numbers to decimal numbers
    roman_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # stores the final result
    final_number = 0
    # for every roman number
    for i in range(len(rnum)):
        # if its not the last number check if the next number is bigger than the current one
        if i != len(rnum) - 1 and roman_dic[rnum[i]] < roman_dic[rnum[i + 1]]:
            # if it is, subtract the current number to the next number and add the result to the final number
            final_number += roman_dic[rnum[i + 1]] - roman_dic[rnum[i]]
            continue
        # if its not the first number and the number before is smaller, continue
        # (means that this number was already used on a subtraction)
        if i != 0 and roman_dic[rnum[i]] > roman_dic[rnum[i - 1]]:
            continue
        # else, add the number to the final number
        final_number += roman_dic[rnum[i]]
    return final_number


print(roman_numeral("MCMXC"))
