"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values
between 0..255 (included).
Input to the function is guaranteed to be a single string.
Note: leading zeros (e.g. 01.02.03.04) are considered not valid.
"""


def ip_validator(ip_num):
    # list of numbers
    num_list = ip_num.split(".")
    # if the ip doesn't have 4 decimal bytes return invalid
    if len(num_list) != 4:
        return "Invalid"
    # for every decimal byte
    for i in num_list:
        # if its > 255 or < 0 return invalid
        if int(i) > 255 or int(i) < 0:
            return "Invalid"
        # if its composed by more than one digit and the first one is a 0 return Invalid
        if len(i) > 1 and i[0] == "0":
            return "Invalid"
    # if everything is fine return valid
    return "Valid"


print(ip_validator("123.45.67.8"))
