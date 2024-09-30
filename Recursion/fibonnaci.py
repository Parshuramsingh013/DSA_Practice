    ## calculate the fibonnaci
def fibonnaci(n):
    if n <=1:
        return n
    return fibonnaci(n-1)+fibonnaci(n-2)

print(fibonnaci(6))