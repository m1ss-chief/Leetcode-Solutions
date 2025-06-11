class Solution:
    def beautySum(self, s: str) -> int:
        def beauty(word):
            freq = {}
            for i in range(len(word)):
                if word[i] not in freq:
                    freq[word[i]] = 1
                else:
                    freq[word[i]] += 1
            beauty = max(freq.values()) - min(freq.values())
            
            return beauty
        sum_beauty = 0
        for i in range(len(s)):
            word = s[i]
            for j in range(i+1,len(s)):
                word += s[j]
                
                b = beauty(word)
                
                if b!= 0:
                    sum_beauty += b
        return sum_beauty

        