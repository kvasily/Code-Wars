"""
We want an array, but not just any old array, an array with contents!

Write a function that produces an array with the numbers 0 to N-1 in it.

For example, the following code will result in an array containing the numbers 0 to 4:

arr(5) // => [0,1,2,3,4]
"""

def arr(n=0): 
    # [ the numbers 0 to N-1 ]
    return [x for x in range(n)]
    
# If n is not set a defualt value of 0 there will be one test that fails
# as the parameter is optional some user will find a way to mess it up

# Best answer:
# Mine was only second best!
"""
def arr(n=0): 
    return list(range(n))
"""

# Examples:
"""
arr=[]
arr = [0 for i in range(5)] 
print(arr)

output [0, 0, 0, 0, 0]
"""