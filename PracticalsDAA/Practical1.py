def iterative_fibonacci(n):
    if n <= 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1

    fib = [0, 1]
    print(0)
    print(1)
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
        print(fib[-1])
    return fib[-1]

def recursive_fibonacci(n, fib_list=None):
    if fib_list is None:
        fib_list = [0, 1]
    if n < len(fib_list):
        return fib_list[n]
    else:
        fib_number = recursive_fibonacci(n-1, fib_list) + recursive_fibonacci(n-2, fib_list)
        if n == len(fib_list):
            fib_list.append(fib_number)
            print(fib_number)
        return fib_number

# Helper function to initialize the recursive approach
def print_recursive_fibonacci(n):
    fib_list = [0, 1]
    for i in range(n + 1):
        if i < len(fib_list):
            print(fib_list[i])
        else:
            recursive_fibonacci(i, fib_list)

# Example usage
print("Iterative Approach:")
iterative_fibonacci(10)
print("\nRecursive Approach:")
print_recursive_fibonacci(10)




# Analysis of Time and Space Complexity: 
# Iterative Fibonacci: Time Complexity: O ( n ) 
# because we compute each Fibonacci number once. 
# Space Complexity: O ( n ) due to the list storing 
# the Fibonacci sequence. It can be reduced to O ( 1 ) 
# if we only keep the last two numbers. Recursive Fibonacci:
# Time Complexity: O ( 2 n ) due to the exponential number of
# recursive calls. Space Complexity: O ( n ) because of the 
# recursion stack depth.