class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res =[0] * n
        pos_index = 0
        neg_index = 1
        for i in range(0,n):
            if nums[i] >= 0:
                res[pos_index] = nums[i]
                pos_index += 2
            else:
                res[neg_index] = nums[i]
                neg_index += 2
        return res

        