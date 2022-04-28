import bt
import time

bt = bt.BT("client")

bt.sync()

while (1):
    bt.send(bt.rooster, "a")
    time.sleep(1)
