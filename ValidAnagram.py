'''
242. Valid Anagram
Given: 2 strings s and t, return true if t is an anagram of s, and false otherwise.

Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1st thing you should do to check if the given is indeed an Anagram:
        # check if the lengths of if the strings s and t are equal
        if len(s) != len(t):
            return False  # is not an anagram

        # Then they are the same length so:
        # dictionaries to store character counts
        char_count_s = {}
        char_count_t = {}
        # Update character counts for string s
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        # Update character counts for string t
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Compare character counts
        return char_count_s == char_count_t


solution = Solution()
# Input: s = "anagram", t = "nagaram"
result1 = solution.isAnagram("anagram", "nagaram")  # result1 should return True!
result2 = solution.isAnagram("rat", "car")  # result2 should return FALSE!

'''
[BREAKDOWN]

Length Check:
if len(s) != len(t):
    return False  # Not an anagram
------------------------------------------------------------
Character Counting:
char_count_s = {}
char_count_t = {}

for char in s:
    char_count_s[char] = char_count_s.get(char, 0) + 1

for char in t:
    char_count_t[char] = char_count_t.get(char, 0) + 1

These loops iterate through each character in strings s and t, updating the character counts in dictionaries char_count_s and char_count_t.
------------------------------------------------------------
Compare:
return char_count_s == char_count_t

This line compares the dictionaries char_count_s and char_count_t.
 If they are equal, it means that the character counts for each character in both strings are the same, 
 and the function returns True, indicating that the strings are anagrams.


BASICALLY, after the lengths of the strings are determined to be equal.
The s and t dicts keep count of the occurences of specific characters.
After that they compar to see if they are the same.
 (it doesnt matter the order, it only matters that they both have the same characters the same amount of time!)

'''