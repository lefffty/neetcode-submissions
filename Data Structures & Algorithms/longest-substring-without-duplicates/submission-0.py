class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_index = {}
        window_start = 0
        length = 0

        for window_end in range(len(s)):
            if (
                s[window_end] in character_index
                and character_index[s[window_end]] >= window_start
            ):
                window_start = character_index[s[window_end]] + 1
            else:
                length = max(
                    length,
                    window_end - window_start + 1
                )
            character_index[s[window_end]] = window_end

        return length