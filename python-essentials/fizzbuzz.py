'''
This code takes a positive integer `A` as input and generates an array of strings according to the FizzBuzz rules. 
It iterates from 1 to `A`, and for each number, it checks if it's divisible by 3, 5, both, or none and appends the
corresponding string to the result array. Finally, it returns the result array.
'''
def fizzBuzz(A):
    result = []
    for i in range(1, A+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Example usage:
A = int(input("Enter a positive integer: "))
print(fizzBuzz(A))


