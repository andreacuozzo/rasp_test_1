## Control DMX moving light with OLA and OpenCV on Raspberry PI Zero W with PICamera

Just started playing with it, I wouldn't touch this guide/code with a stick.

### My scenario

- Raspberry PI Zero W with Raspberry PI Camera Rev. 1.3 https://www.amazon.it/Modulo-fotocamera-webcam-supporta-Raspberry/dp/B0748FZXW3
- Samsung Evo Plus 32 GB mmc with Raspberry Pi OS (32-bit) with desktop and recommended software  https://www.raspberrypi.org/downloads/raspberry-pi-os/
- Briteq BT-70l clone moving light https://briteq-lighting.com/bt-70ls
- USB-2-DMX cable https://www.amazon.it/DSD-TECH-Adattatore-Controller-apparecchio-Illuminazione/dp/B07WV6P5W6

### Setup Raspberry Pi and OLA

```
sudo su

raspi-config

  ## enable camera
  ## enable ssh
  ## enable vnc

apt-get update && apt-get upgrade

apt-get install ola

# disable this (thx to https://youtu.be/3rJIqyxE3aY)

sed -i 's/enabled = true/enabled = false/' /etc/ola/ola-opendmx.conf
sed -i 's/enabled = true/enabled = false/' /etc/ola/ola-usbserial.conf

# enable this

sed -i 's/enabled = false/enabled = true/' /etc/ola/ola-ftdidmx.conf

# connect moving head
# Add Universe using th web interface http://192.168.1.19:9090/ola.html

 ## Reload Plugins
 ## Add Universe: id=1, name=test, device=FT232R USB UART with serial number : AB0K9VXG

```

### Motion tracking with OpenCV

Thanks to: https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/

```
# Packages required for OpenCV

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools libatlas-base-dev

# Older version of OpenCV because version 4 has errors
pip3 install opencv-python==3.4.6.27
```

### Testing: testsocket.py

Listens on socket 10002 on ip 192.168.1.19 for tcp pakets, and runs ola_streaming_client (comes with OpenCv) accordingly, ie:

ola_streaming_client -u 1 -d 85,,50  <-- 85 left-right; 50 up-down

```
python testsocket.py
```

#### Testing: color.py

Capture video from the picamera, and for each frame:
 - draws a rectangle on the blue object
 - gets the rectangle center coordinates
 - moves the moving head accordingly
```
python3 color.py
```
