
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        m = 10

        if n < m:
            return []

        BASE = 256
        MOD = 10**9 + 7

        power = pow(BASE, m - 1, MOD)

        dnaHash = 0

        # Hash the first window
        for idx in range(m):
            dnaHash = (dnaHash * BASE + ord(s[idx])) % MOD

        # Store actual sequences for collision safety
        dna = {}
        repeated = set()
        ans = []

        for right in range(n - m + 1):

            window = s[right:right + m]

            if dnaHash not in dna:
                dna[dnaHash] = set()

            # Check whether this exact sequence appeared before
            if window in dna[dnaHash]:
                if window not in repeated:
                    ans.append(window)
                    repeated.add(window)
            else:
                dna[dnaHash].add(window)

            # Always roll the hash, even if the window is repeated
            if right < n - m:
                outgoing = ord(s[right])
                incoming = ord(s[right + m])

                dnaHash = (
                    dnaHash - outgoing * power
                ) % MOD

                dnaHash = (
                    dnaHash * BASE + incoming
                ) % MOD

        return ans
