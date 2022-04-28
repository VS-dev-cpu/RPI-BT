import bt
import time

print("waiting...")
bt = bt.BT("server")

time.sleep(2)

print("go")

bt.start()

while (1):
    addr, a = bt.receive()
    print("From " + str(addr) + " Received: " + str(a))
