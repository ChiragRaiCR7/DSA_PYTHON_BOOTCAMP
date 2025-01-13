def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    lst=[]
    lts=["*"*n]
    for i in range(n):
        lst+=lts
    print(lst)
n=int(input("Enter a Number"))
generate_square(n)