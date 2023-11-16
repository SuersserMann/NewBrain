s = "   -42"


def myAtoi(s):
    for i in range(len(s)):
        if s[i] != " ":
            s = s[i:]
            break

    result = []
    pos = True
    if len(s) >= 2:
        if s[0] == "-" and s[1].isdigit():
            pos = False
        elif s[0] == "+" and s[1].isdigit():
            pos = True
        elif s[0].isdigit():
            ()
        else:
            return 0
    elif s == "":
        return 0
    elif len(s) == 1 and s[0].isdigit():
        return int(s)
    else:
        return 0

    for i in range(len(s)):
        if not s[i].isdigit():
            if i == 0:
                continue
            else:
                if result == []:
                    return 0
                else:
                    break
        else:
            result.append(s[i])
    result = int("".join(result))
    if not pos:
        result = -result
        if result <= -2 ** 31:
            return -2 ** 31
        else:
            return result
    else:
        if result >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result


print(myAtoi(s))
