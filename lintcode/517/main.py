# def isUgly(num: int) -> bool:
#     print(num)
#     if num == 0: return False;
#
#     if num == 1 or num == 2 or num == 3 or num == 5:
#         return True
#
#     cond1, cond2, cond3 = False, False, False
#
#     if num % 2 == 0:
#         cond1 = isUgly(num // 2)
#     elif num % 3 == 0:
#         cond2 = isUgly(num // 3)
#     elif num % 5 == 0:
#         cond3 = isUgly(num // 5)
#
#     return cond1 or cond2 or cond3
#
#
# x = isUgly(14)


def isUgly(num: int) -> bool:
    print(num)
    if num == 0: return False
    if num == 1 or num == 2 or num == 3 or num == 5: return True;

    c = False;

    for multiplier in [2, 3, 5]:
        if num % multiplier == 0:
            c = c or isUgly(num // multiplier)
            if c is True:
                break;
    return c


print(isUgly(91125))