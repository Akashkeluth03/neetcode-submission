class Solution:
    def removeDuplicates(self, num: List[int]) -> int:
        n = len(num)
        if num == 1:
            return 1
        i = 0
        j = i+1
        while j < n:
            if num[j] != num[i]:
                i+=1
                num[i],num[j] = num[j],num[i]
            j+=1
        return i+1


        