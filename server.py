import bt
import time

bt = bt.BT("server")

time.sleep(2)

bt.start()

while (1):
    addr, a = bt.receive()
    print("From " + str(addr) + " Received: " + str(a))
