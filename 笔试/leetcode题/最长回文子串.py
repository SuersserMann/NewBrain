s = "bb"


def longestPalindrome(s):
    x = len(s)
    max = 0
    result=s[0]
    for i in range(x):
        cur = s[i]
        a = 1
        while i - a >= 0 and x - i - a-1 >= 0:
            if s[i - a] == s[i + a]:
                cur = s[i - a:i + a + 1]
                a += 1
            else:
                break

            if len(cur) > max:
                result = cur
                max = len(cur)

    for i in range(x):
        cur = s[i]
        a = 1
        while i - a >= 0 and x - i - a >= 0:
            if s[i - a] == s[i + a - 1]:
                cur = s[i - a:i + a]
                a += 1
            else:
                break

            if len(cur) > max:
                result = cur
                max = len(cur)

    return result


print(longestPalindrome(s))
