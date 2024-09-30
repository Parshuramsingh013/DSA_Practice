# def ajit():
#     print("1")
#     ajit()

# ajit()


count = 1

def ajit(n):
    global count
    if count == n+1:
        return
    print(count)
    count += 1
    ajit(n)

ajit(10)