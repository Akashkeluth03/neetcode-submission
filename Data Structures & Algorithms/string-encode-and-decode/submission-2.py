class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the index of the '#' delimiter
            while s[j] != "#":
                j += 1
                
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # Slice the actual string and add to results
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the main pointer 'i' to the start of the next encoded string
            i = j + 1 + length
            
        return res