i = 0
count = 0
while True:
    n = int(input())
    i +=1
    if n == 0:
        print("     ",count)
        exit()
    elif n == i:
        count +=1
