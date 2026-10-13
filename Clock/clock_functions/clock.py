import time

def Clock():
    print("Press CTRL+C to exit")
    try:
        while True:
            print(time.strftime("%H:%M:%S"),end=" ",flush=True)
            time.sleep(1)
            print("\r",end=" ",flush=True)
    except KeyboardInterrupt:
        print("\nThanks for coming\n")

def Timer():
    print("Timer is started.Press CTRL + C to exit")
    try:
        second = int(input("Enter Second: "))
    except:
        print("Invalid Input")
        return
    try:
        while second > 0:
            mins ,sec = divmod(second,60)
        
            print(f"\r{mins:}:{sec:}",end="",flush=True)
            time.sleep(1)
            second -= 1
        print("\nTimes up!")
    except KeyboardInterrupt:
        print("\nThanks for coming\n")

def Stopwatch():
    print("Press CTRL+C to exit")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins ,sec = divmod(int(elapsed),60)
            print(f"\r{mins:02}:{sec:02}", end="", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nThanks for coming.\n")


if __name__ == "__main__":
    Clock()
    Timer()
    Stopwatch()