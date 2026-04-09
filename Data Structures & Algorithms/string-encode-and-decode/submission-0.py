class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s  
            #have integer indicate start of the string, and the length after that is the message
            #have # to indicate the start of the message
        return res

 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': #stopping condition
                j += 1
            length = int(s[i:j]) #0 until # is our length
            i = j + 1 #string after the # is the start
            j = i + length #start + length = end
            res.append(s[i:j])
            i = j

        return res
