class Solution:
    # @param words: list of strings
    # @return: integer (number of similar pairs)
    def countPairs(self, words):
        """
        Count pairs of similar strings.
        Similar if they can be made equal by cyclic letter shifts.
        """
        
        # Character to number mapping
        char_to_num = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
        }
        
        # Compute length without len()
        def get_length(s):
            count = 0
            for c in s:
                count = count + 1
            return count
        
        # Subtract modulo 26
        def sub_mod26(a, b):
            result = a - b
            while result < 0:
                result = result + 26
            return result
        
        # Dictionary to store pattern frequencies
        pattern_count = {}
        
        for word in words:
            n = get_length(word)
            
            # Single character: store the character itself
            if n == 1:
                key = (word[0],)
            else:
                # Convert characters to numbers
                nums = []
                for ch in word:
                    nums.append(char_to_num[ch])
                
                # Compute relative differences from first character
                first = nums[0]
                pattern = []
                for i in range(n):
                    diff = sub_mod26(nums[i], first)
                    pattern.append(diff)
                
                key = tuple(pattern)
            
            # Count frequency
            if key in pattern_count:
                pattern_count[key] = pattern_count[key] + 1
            else:
                pattern_count[key] = 1
        
        # Calculate total pairs
        total_pairs = 0
        for count in pattern_count.values():
            pairs = count * (count - 1) // 2
            total_pairs = total_pairs + pairs
        
        return total_pairs


# ============================================
# Test cases (for local testing)
# ============================================

# Create instance
sol = Solution()

# Test 1
words1 = ["fusion", "layout"]
result1 = sol.countPairs(words1)
print("Test 1: " + str(result1))  # Expected: 1

# Test 2
words2 = ["ab", "aa", "za", "aa"]
result2 = sol.countPairs(words2)
print("Test 2: " + str(result2))  # Expected: 2

# Test 3
words3 = ["a", "b", "c", "a"]
result3 = sol.countPairs(words3)
print("Test 3: " + str(result3))  # Expected: 3

# Test 4
words4 = ["ab", "cd", "ef"]
result4 = sol.countPairs(words4)
print("Test 4: " + str(result4))  # Expected: 0
