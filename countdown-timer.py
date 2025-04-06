import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")


t = input("Enter the time in seconds: ")
try:
    t = int(t)
    countdown(t)
except ValueError:
    print("Please enter a valid integer for the time in seconds.")
