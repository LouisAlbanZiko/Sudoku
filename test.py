import time, sys
def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[10D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()
