class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "?" + string
        return encodedString
        

    def decode(self, s: str) -> List[str]:
        decodedArray = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != "?":
                j += 1
            length = int(s[i:j])  
            word = s[j + 1 : j + 1 + length]  
            decodedArray.append(word)
            i = j + 1 + length                 

        return decodedArray
