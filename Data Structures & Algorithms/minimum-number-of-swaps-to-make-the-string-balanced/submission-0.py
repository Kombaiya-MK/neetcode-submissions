class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        swaps = 0
        isClosedWithoutOpen = 0
        isOpenWithoutClosed = 0
        for ch in s:
            if ch == ']':
                if st and st[-1] != '[':
                    isClosedWithoutOpen += 1
                elif st:
                    st.pop()
                else:
                    st.append(ch)
            else:
                if st and st[-1] == ']':
                    isOpenWithoutClosed += 1
                else:
                    st.append(ch)
        swaps = (isOpenWithoutClosed + isClosedWithoutOpen) // 2
        # print(st)
        # print(swaps)
        return swaps
        