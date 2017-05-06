import time
from feed import feed

def main():
    f = feed()
    f.start()
    for i in range(0,10):
        f.take_still()
        time.sleep(2)

if __name__ == "__main__":
    main()
