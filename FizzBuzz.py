# This problem is essentially asking you to make a function that takes a user input "n" and return a array that would count up to the input number (ex 3,5,15)
# the list would contain any amount of numbers ranging 1 to n
# n being 15 would return... 15 indicies of results

# Explanation:
# 3: if a number is divisible by 3, replace that number with Fizz. If currentNumber % 3 equals 0....  then currNumber is set to Fizz

# 5: if a number is divisible by 5, replace that number with Buzz. If currentNumber % 5 equals 0....  then currNumber is set to Buzz

# 3,5 if a number is divisible by both 3 and or by 5, replace that number with FizzBuzz and add that to the list. If currentNumber % 5 equals 0....  then currNumber is set to FizzBuzz and is added to list.

# not 3 & not 5: if a number is NOT divisible by both 3 and 5, append that number with on to the list.
# if currentNumber % 5 (and or 3) equals 0.... then currNumber is just added to output list.


class Solution(object):
    def fizzBuzz(self, n):
        # make an empty array that would be used to store the output result
        output = []

        # create a for loop 1 to n (n being the input number)
        for i in range(1, n + 1):
            # create variables to check for when i (the current n)
            # is divisible by the respective number
            fizz = i % 3 == 0
            buzz = i % 5 == 0

            if fizz and buzz:
                output.append("FizzBuzz")
            elif fizz:
                output.append("Fizz")
            elif buzz:
                output.append("Buzz")
            else:
                output.append(str(i))
        return output


solution_instance = Solution()
#  ["1", "2", "Fizz"]
print(solution_instance.fizzBuzz(3))

#  ["1", "2", "Fizz", "4", "Buzz"]
print(solution_instance.fizzBuzz(5))

# ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
print(solution_instance.fizzBuzz(15))
