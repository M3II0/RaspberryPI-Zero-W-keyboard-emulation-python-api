# RaspberryPI Zero W (Creating Keyboard HID device)
How to create HID keyboard with your Raspberry PI Zero W

## Requirements
- Raspberry PI Zero W (That's what I'm using) | https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ |
- Raspberry PI Zero W USB Addon | https://botland.com.pl/produkty-wycofane/12480-pi-zero-w-usb-a-addon-board-v11-nakladka-dla-raspberry-pi-zerozero-w.html |
- Wifi connection
- Micro-SD Card (I recommend 32GB)
- (Optional) Micro-SD Card reader, to read/write data into it from PC

## Raspberry PI Zero W (Setup) - Installing RaspberryOS on Micro-SD card from PC
- Download https://www.raspberrypi.com/software/
- Run program on PC
- Install RaspberryOS-Lite (Just debian)
  
![image](https://github.com/M3II0/RaspberryPI-Zero-W-keyboard-emulation/assets/73041364/19d2f6cc-3fe4-437f-89a9-ce4f65bd6582)

- Configure WAN connection to your WIFI & SSH details (You'll need them)
  
![image](https://github.com/M3II0/RaspberryPI-Zero-W-keyboard-emulation/assets/73041364/59576d39-1720-416c-bf16-b7780df4b1b4)

- Click save
- Choose your Micro-SD card and click WRITE
- (Wait until OS will be installed on card)
- Remove card, and insert into Raspberry PI Zero W

## First run
- Plug Raspberry PI Zero W (RPZW) into PC (If you didn't install USB addon, do it) - USB Addon will be plug & dispatcher (Don't worry about pwoer supply)
- Wait a few minutes until your RPZW starts, and connects to Wifi (You can check it in your router administration)

## Logging in with PuTTy through SSH
- Download PuTTy if you don't have it | https://www.putty.org/ |
- Open and insert here local IP adress of RPZW (Can be found in router administration), port should be 22
- After connecting you'll be asked for user & password (Insert SSH details that you writed in OS configuration)

## Prepare USB modules
- Run commands

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt

echo " eeee" | sudo tee -a /boot/commandLine.txt

echo "dwc2" | sudo tee -a /etc/modules

sudo echo "libcomposite" | sudo tee -a /etc/modules

sudo touch /usr/bin/isticktoit_usb

sudo nano /etc/rc.local

- Add the following before the line containing exit 0

/usr/bin/isticktoit_usb

- Run command

sudo nano /usr/bin/isticktoit_usb

- Insert here this text & save

```#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p isticktoit
cd isticktoit
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "fedcba9876543210" > strings/0x409/serialnumber
echo "Tobias Girstmair" > strings/0x409/manufacturer
echo "iSticktoit.net USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC
```
