import bt
import time

bt = bt.BT("server")

while (1):
    addr, a = bt.receive()
    print("From " + str(addr) + " Received: " + str(a))
