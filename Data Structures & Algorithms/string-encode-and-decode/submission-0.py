class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            encodedString += string + str(len(string)) + "?"
        return encodedString
        

    def decode(self, s: str) -> List[str]:
        decodedArray = []
        k = 0
        for i in range(len(s)):
            if s[i].isdigit():
                decodedArray.append(s[k:i])
                k = i + 2

        return decodedArray[:len(decodedArray)]
