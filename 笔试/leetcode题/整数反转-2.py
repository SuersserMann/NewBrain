x = 5970


class Solution:
    def reverse(self, x):

        if x >= 0:
            c = str(x)
            cur = 0
            for i in range(len(c) - 1, -1, -1):
                if c[i] == '0':
                    cur += 1
                else:
                    break
            c = c[len(c) - cur - 1::-1]
            c=int(c)
            if c > 2 ** 31:
                return 0
            return c
        else:
            c = str(x)
            cur = 0
            for i in range(len(c) - 1, -1, -1):
                if c[i] == '0':
                    cur += 1
                else:
                    break

            c = '-' + c[len(c) - cur - 1:0:-1]
            c = int(c)
            if c < (-1) * 2 ** 31:
                return 0
            return c

s=Solution()
print(s.reverse(x))
