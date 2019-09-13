class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False
        if x == 0:
            return True

        new_x = []
        while x > 0:
            new_x.append(str(x % 10))
            x = x // 10
        result = ''.join(new_x)

        return True if result == result[:: -1] else False  # new_s_list[:: -1]列表反转


if __name__ == '__main__':
    x = 10
    S = Solution()
    print(S.isPalindrome(x))