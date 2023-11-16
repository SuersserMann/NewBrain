s = "PAYPALISHIRING"
numRows = 2


def convert(s, numRows):
    if numRows == 1:
        return s
    n = 2 * numRows - 2
    result = [""] * numRows
    for i, char in enumerate(s):
        x = i % n
        result[min(x, n - x)] += char
    return "".join(result)


print(convert(s, numRows))
