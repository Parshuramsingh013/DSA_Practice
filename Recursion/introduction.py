def ajit():
    print("1")
    ajit()

ajit()


count = 0

def ajit():
    global count
    if count == 4:
        return
    print(count)
    count += 1
    ajit()

ajit()