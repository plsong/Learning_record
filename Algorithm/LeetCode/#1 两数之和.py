class Solution:
    def twoSum(self,nums,target):
        hash_map = dict()
        for i,x in enumerate(nums):
            if target-x in hash_map:
                return [hash_map[target-x],i]
            hash_map[x] = i

if __name__ == '__main__':
    nums = [1,5,6,4]
    target=9
    S = Solution()
    print(S.twoSum(nums,target))


