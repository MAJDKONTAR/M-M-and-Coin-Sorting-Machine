# M&M and Coin Sorting Machine
![image](https://user-images.githubusercontent.com/97162452/158182709-8965c9ba-f466-4cc0-bde3-af54a0371654.png)
## Description
A simple M&M and coin sorting machine using computer vision and a Raspberry Pi. This low cost sorting machine utilizes two Rover 5s acting as conveyer belts with a RPi camera being the sensor for performing the classification.

## Hardware Connections
![image](https://user-images.githubusercontent.com/97162452/158183636-67cf9cef-bfa8-4497-947a-1a96d1b2e420.png)

## Modes of Operation

### Coin Sorting
*Video Demo*
[![Watch the video](https://img.youtube.com/vi/Gx_8bvQIUb0/maxresdefault.jpg)](https://youtu.be/Gx_8bvQIUb0)
The coin is placed is placed on the first conveyer belt, it is then moved forward until it becomes visible to the camera. After that, the camera detects the size and color of the coin. Based on the values obtained, the Raspberry Pi moves the coin to the corresponding box.

### M&Ms Sorting
*Video Demo*
[![Watch the video](https://img.youtube.com/vi/MibJyXAaTx4/maxresdefault.jpg)](https://youtu.be/MibJyXAaTx4)
The M&M is placed is placed on the first conveyer belt, it is then moved forward until it becomes visible to the camera. After that, the camera detects the color of the M&M. Based on the values obtained, the Raspberry Pi moves the candy to the corresponding box.

## Color Detection
![image](https://user-images.githubusercontent.com/97162452/158188495-9d291c92-2439-4967-86c0-87c92f7eddca.png)
<p>To identify the color of the object a mask with the RGB values was applied to the image.</p>

## Size detection
![image](https://user-images.githubusercontent.com/97162452/158188865-c6757c48-83e3-47d3-9311-02e62ac1d038.png)
<p>To identify teh size of the object, we first need to calibrate our system. This is done by adding a reference object in which all the other objects are compared to. In this project the conveyer belt was used as the reference. Measurements of its height and width were inputted to the code. Finally, using opencv the contour of the object is detect and thus the size of the object is obtained.</p>

## Future Work

* Use of a wider conveyor belt such that we can add bigger objects to classify, not just small items.
* Use of a controller with faster processing, than the Raspberry Pi model 3B, one option could be the Raspberry Pi 4 model B which possesses much higher processing capabilities, or just use a completely different microcontroller, or even desktop grade hardware microcontrollers.
* Automating the insertion process, in our project we manually place the object on the conveyor, a better way is to use gates using either pneumatic switches or servo motors, coupled with proximity sensors such as ultra sound sensors to automate the opening and closing of the gates.
* Adding more categories of classification, and also building a system that can accommodate that.
