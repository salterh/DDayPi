# DDayPi

## Spec 

An interactive escape room experience in where users must listen closely to their surroundings and handheld device for clues. Uses Raspberry Pis and connected circuits as the main interactive element.

## Raspberry Pi Setup
This guide assumes you have a fresh install of Raspberry Pi (previously Raspbian) Bullseye. If you have not done this, you can find instructions [here](https://www.raspberrypi.com/software/).

- Open the Command Line Interface (CLI) and type in:
- sudo date --set='yearmonthday hour:minute' && reboot
	- e.g. sudo date --set='20221125 10:51' && reboot

- Connect to WiFi. 

- Open the CLI and type in:
- sudo apt update
- sudo apt upgrade
- sudo apt install puredata
- pip3 install schedule
- pip3 install oscpy
- git clone https://github.com/pimoroni/pirate-audio 
  cd pirate-audio/mopidy
  sudo ./install.sh
- cd
- git clone https://github.com/salterh/DDayPi.git

- Depending on what code you want to run on boot, the absolute paths will change. These changes are marked with <>, and this example will use the Morse puzzle.
- Open the CLI and type in:
	cd
	sudo nano /etc/xdg/autostart/<morse>.desktop
	
	- Copy and paste the following:
		- [Desktop Entry]
		- Type=Application
		- Exec=sudo bash /home/pi/DDayPi/Morse/morse.sh
		- StartupNotify=false
		- Terminal=false

	- Ctrl + S, then Ctrl + X to save and exit.

- Reboot and test

- Occassionally, for programs that run Puredata, it will fail to open from the bash scripts (Unsure why; the error message are unhelpful). 
- In this case, you should make two seperate .desktop files; one to launch the Puredata patch and another to launch the python3 script.
- Open the CLI and type in:
	cd
	sudo nano /etc/xdg/autostart/<handheld>.desktop

	- Copy and paste the following:
		- [Desktop Entry]
		- Type=Application
		- Exec=puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" /home/pi/DDayPi/Handheld/handheld.pd
		- StartupNotify=false
		- Terminal=false

	- Ctrl + S, then Ctrl + X to save and exit.

	cd
	sudo nano/etc/xdg/autostart/<handheldPy>.desktop
	
	- Copy and paste the following: 
		- [Desktop Entry]
		- Type=Application
		- Exec=python3 /home/pi/DDayPi/Handheld/handheld.py
		- StartupNotify=false
		- Terminal=false

	- Ctrl + S, then Ctrl + X to save and exit.

- Reboot and test
