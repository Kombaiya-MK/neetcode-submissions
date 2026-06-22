class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resultStr = strs[0]

        for i in range(1, len(strs)):
            str2 = strs[i]
            m = min(len(resultStr), len(str2))
            j = 0
            while j < m:
                if resultStr[j] == str2[j]:
                    j += 1
                else:
                    break
                    
            resultStr = resultStr[:j]
            
        return resultStr


        