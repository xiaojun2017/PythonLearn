import sys
import time

f = None
try:
    f = open("open.txt")
    while True:
        line = f.readline();
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.sleep(2)
except IOError:
    print("IOError occur. ")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
