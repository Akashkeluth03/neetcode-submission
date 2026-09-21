class Solution:
    def removeElement(self, num: List[int], val: int) -> int:
        k = 0
        for i in range(len(num)):
            if num[i] != val:
                num[k] = num[i]
                k +=1
        return k


        