import os
import bluetooth

class BT():
    def __init__(self, hostname):
        
        os.system("bluetoothctl discoverable on")
        
        mac_rpi0_samu = "B8:27:EB:48:52:95"    #RPI0
        mac_rpi3_samu = "B8:27:EB:10:0D:19"    #RPI1
        mac_rpi4_samu = "DC:A6:32:6B:3A:AB"    #RPI2
        
        mac_rpi4_zeti = "DC:A6:32:78:BC:C7"    #RPI3
        mac_rpi4_mate = "DC:A6:32:25:D2:CC"    #RPI4
        
        self.rooster = mac_rpi3_samu
        self.pig1 = mac_rpi4_samu
        self.pig2 = mac_rpi4_zeti
        self.pig3 = mac_rpi4_mate
      
        if (hostname == "server"):
            self.sync()
            self.sync()
            self.sync()
                
        elif (hostname == "client"):
            en = False
            while not en:
                en = self.send(self.rooster, "asd")
            
        else:
            pass
    
    def receive(self):
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
          
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)
          
        client_sock,address = server_sock.accept()
          
        data = client_sock.recv(1024)
          
        client_sock.close()
        server_sock.close()
          
        return address[0], data;
      
    def send(self, targetBluetoothMacAddress, message):
        try:
            sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            sock.connect((targetBluetoothMacAddress, 1))
            sock.send(message)
            sock.close()
            return True
        except:
            return False
        
    def sync(self):
        return self.receive()

    def start(self):
        self.send(self.pig1, "start")
        self.send(self.pig2, "start")
        self.send(self.pig3, "start")
