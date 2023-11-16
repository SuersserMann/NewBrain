s = "accaaccaaaab"

dict = {}


def lengthOfLongestSubstring(s):
    start = -1
    max = 0
    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = i
            result = i - start
            if result >= max:
                max = result
        else:
            result = i - start-1
            start = i
            if result >= max:
                max = result
            dict[s[i]] = i
    return max


print(lengthOfLongestSubstring(s))
print(dict)
