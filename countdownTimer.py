import time

def countdown(start=10):
    for i in range(start, -1, -1):  # Start at 10, stop at -1 (so it includes 0), step by -1
        print(i)
        time.sleep(3)  # Wait for 1 second

if __name__ == "__main__":
    countdown()
