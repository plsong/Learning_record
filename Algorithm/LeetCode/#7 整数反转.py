
class Solution(object):
    def reverse(self,x):

        # 特殊情况，x=0
        if x==0:
            return 0

        # 一般情况
        is_negative=False
        if x<0:
            is_negative=True
            x=-x

        new_x=[]
        while x>0:
            new_x.append(str(x%10))
            x = x//10
        if is_negative:
            result='-'+''.join(new_x)
        else:
            result=''.join(new_x)
        result=int(result)

        # 特殊情况，溢出
        if (result>2**31-1) or (result<-2**31):
            return 0
        else:
            return result

if __name__ == '__main__':
    x=-15
    S=Solution()
    print(S.reverse(x))