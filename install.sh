echo "Installing Libs for Bluetooth"

sudo apt install pip

sudo apt-get install bluetooth bluez libbluetooth-dev
sudo python3 -m pip install pybluez

mv pystart.py ..
sudo echo "python3 ~/pystart.py" >> ~/.bashrc
