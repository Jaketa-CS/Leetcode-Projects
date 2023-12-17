'''
3. Longest Substring Without Repeating Characters

Given: string s,
Find: the length of the longest substring without repeating characters.
substring: a contiguous non-empty sequence of characters within a string.

longest and repeating keywords hint us that its a sliding window problem
    --> https://builtin.com/data-science/sliding-window-algorithm
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #initialize 2 pointers variables for the sliding window
        left_pointer  = 0
        right_pointer = 0


        #initialize a dict to stor the last seen index of each char
        char_dict = {}
        #initialize the variable to store the length of the longest substring
        longest_substring_length = 0

        #start to iterate through the s string with the right pointer
        while right_pointer < len(s):
            #check if the character currently at the right pointer is in the dictionary
            if s[right_pointer] in char_dict and char_dict[s[right_pointer]] >= left_pointer :
               #character is in dict, so move the left pointer ro the right of the last seen index
               left_pointer  = char_dict[s[right_pointer]] + 1 #+1 to move right an index
            #Update the last seen/saved index of the character in the dictionary
            char_dict[s[right_pointer]] = right_pointer # at the start rightPointer = 0...
                                                        # NOW rightPointer is the  last seen index

            #Update the current longest substrings length if the current substring is longer
            if right_pointer - left_pointer  + 1 > longest_substring_length:
                longest_substring_length = right_pointer - left_pointer  + 1

            #move the right pointer over to the next index (the next character)
            right_pointer += 1
        return longest_substring_length

solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
result2 = solution.lengthOfLongestSubstring("bbbbb")
result3 = solution.lengthOfLongestSubstring("pwwkew")
print ("abcabcbb output: ",result)
print ("bbbbb output: ",result2)
print ("pwwkew output: ",result3)


'''
[PROCESS (for result)]:

Given string: "abcabcbb"
Initialize 2 pointers variables for the sliding window
left_pointer = 0
right_pointer = 0

Initialize a dict to store the last seen index of each char
char_dict = {}

Initialize the variable to store the length of the longest substring
longest_substring_length = 0

Initial state:
"abcabcbb"
 ^
The window starts at index 0.

Iteration 1:
"abcabcbb"
  ^

The right pointer moves to the next character 'b'.
The character 'a' is added to char_dict with its index 0.

left_pointer = 0
right_pointer = 1
char_dict = {'a': 0}

Iteration 2:
"abcabcbb"
  ^
The right pointer moves to the next character 'c'.
The character 'b' is added to char_dict with its index 1.

left_pointer = 0
right_pointer = 2
char_dict = {'a': 0, 'b': 1}

... Continue iterating ...

Iteration 6:
"abcabcbb"
        ^
The right pointer moves to the next character 'b'.
Since 'b' is already in char_dict and its last seen index is >= left_pointer,
move the left pointer to the right of the last seen index (left_pointer = 3).
The character 'b' is updated in char_dict with its new index 6.

left_pointer = 3
right_pointer = 6
char_dict = {'a': 4, 'b': 6, 'c': 5}

Final result:
The longest substring without repeating characters is "abc" with a length of 3

'''

'''
[SUMMARY]

Two pointers, left_pointer and right_pointer, are initialized at the start of the string s.
A dictionary, called char_dict, is initialized to store the last seen index of each character.
The variable longest_substring_length is initialized to 0.

Iteration:
The right_pointer iterates through the string from the start to the end.

For each character at the right_pointer:
If the character is already in char_dict 
and its last seen index is greater than or equal to left_pointer, 
move the left_pointer to the right of the last seen index.

Update the last seen index of the character in char_dict.

Update the length of the current substring if the current substring is longer.

Move the right_pointer to the next index.


Result:
The final result is the length of the longest substring without repeating characters.
'''