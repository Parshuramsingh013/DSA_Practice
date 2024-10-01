    ## Check for the pelindrome

name = "aya"


def checkPelindrome(i,n):
    if i > n//2:
        return True
    if name[i] != name [n-i-1]:
        return False
    return checkPelindrome(i+1,n)


print(checkPelindrome(0,len(name)))

