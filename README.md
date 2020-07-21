# rasp_test_1

My first test with raspberry pi

=== Setup ===

sudo su

raspi-config

  * camera
  * ssh
  * vnc

apt-get update && apt-get upgrade

=== OLA for Moving Head ===

apt-get install ola

# enabled = false

sed -i 's/enabled = true/enabled = false/' /etc/ola/ola-opendmx.conf
sed -i 's/enabled = true/enabled = false/' /etc/ola/ola-usbserial.conf

# enabled = true

sed -i 's/enabled = false/enabled = true/' /etc/ola/ola-ftdidmx.conf

# connect moving head
# Add Universe 

--> http://192.168.1.19:9090/ola.html
--> Reload Plugins
--> Add Universe

  * id=1 
  * name=test
  * device=FT232R USB UART with serial number : AB0K9VXG


=== Motion tracking ===

Using this; https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/

### Preprequisites

# Get packages required for OpenCV

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools libatlas-base-dev

# Need to get an older version of OpenCV because version 4 has errors
pip3 install opencv-python==3.4.6.27

