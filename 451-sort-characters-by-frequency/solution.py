class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        # freq = Counter(s)
        # sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        # result = ""
        # for ch in sorted_chars:
        #     result += ch * freq[ch]
        # return result

        return ''.join(c * freq for c, freq in Counter(s).most_common())
