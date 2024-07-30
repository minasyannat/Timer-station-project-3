import time
try:
    user = input("input a time in the format h:m:s to start the countdown ").split(":")
    user = [int(i) for i in user]
    start = user[2]
    while True:
        for i in range(start, -1,-1):
            timer = f"{user[0]}:{user[1]}:{i}"
            print(timer)
            time.sleep(1)
        start = 59
        user[1] = user[1] - 1
        if user[1] == -1:
            user[1] = 59
            user[0] = user[0] - 1
            if user[0]<0:
                break
except ValueError:
     print("You need to input 3 integer numbers :)")
except IndexError:
    print("Please enter 3 numbers separated by ':' ")