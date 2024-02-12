'''
In this implementation:
The solve method takes an integer A representing a year as input.
It checks two conditions to determine if the year is a leap year:
If the year is divisible by 400, it's a leap year.
If the year is divisible by 4 but not divisible by 100, it's also a leap year.
If any of these conditions are satisfied, the method returns 1 indicating it's a leap year, 
otherwise, it returns 0 indicating it's not a leap year.'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Check if the year is divisible by 400 or divisible by 4 but not divisible by 100
        if (A % 400 == 0) or (A % 4 == 0 and A % 100 != 0):
            return 1  # Return 1 if it's a leap year
        else:
            return 0  # Return 0 if it's not a leap year

# Example usage:
year = int(input("Enter the year: "))  # Input the year from the user
solution = Solution()  # Create an instance of the Solution class
print(solution.solve(year))  # Output the result of whether the year is a leap year or not

