class Solution:
    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for s in strs: # parse through s 
            sentence += str(len(s)) + "#" + s # "5#lolol"
        return sentence

    def decode(self, s: str) -> List[str]:
        res , i = [] , 0 #final return struct, index
        # "2#hi3#hel4#hell"
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1        
            length = int(s[i:j]) # 0:1 = 0 now storing 2
            res.append(s[j+1:j + length + 1])
            i = j + length + 1
        return res