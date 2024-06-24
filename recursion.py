def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
    
def natural(n):
    if n == 1:
        return 1
    else:
        return n + natural(n-1)

def multiply(a,b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b-1)
    
def raise_to(a,b):
    if b == 1:
        return 1/a
    else:
        return 1/a * raise_to(a, b-1)
   
def rec(board, action):
    if 
