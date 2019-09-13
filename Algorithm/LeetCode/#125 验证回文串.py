class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        new_s_list = [index.lower() for index in s_list if index.isalpha() or index.isdigit()] #只保留字母和数字
        return True if new_s_list == new_s_list[:: -1] else False # new_s_list[:: -1]列表反转


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    S=Solution()
    result = S.isPalindrome(s)
    print(result)

'''
几个函数的用法
s.lower()：全部变为小写
s.isalpha()：判断是否是字母
s.isdigit()：判断是否是数字

'''

