# WOA_WOC-Robotic-Arm-Planter
![91kUHCS](https://user-images.githubusercontent.com/66904646/205602779-8f77df30-8a29-470c-a962-31dd8806618b.png)

Team Name :
Geckos

Group members:
1. Ali Al-yasari : s2177303
2. Ahmed Al-yasari : S2002913
3. Yang Zhenyu : s2118292
4. Guo Yuwei : s2168298
5. xiongsen Mo: s2113667
6. Umme Suhaima Bangali ：S2199874



The project consists of raspberry pi 4 modle b and PCA9685 servo controler and the robot arm it self

![GPIO-Pinout-Diagram-2](https://user-images.githubusercontent.com/66904646/220793473-3dd84a81-169a-493f-92ca-89050cfb9b0e.png)
![PCA9685-PWM-Servo-Pinout](https://user-images.githubusercontent.com/66904646/220793575-55928f45-6f9b-413b-9227-598940ef8d48.jpg)

Wiring: 

raspberry pi 4: PCA9685 servo controller

pin(2) 5V power connects to V+

pin(1) 3v3 power connects to vcc

pin(3) GPIO 2 (SDA) connects to SDA

pin(5) GPIO 3 (SCL) connects to SCL

pin(6) Ground connects to GND

code running: 

The two main files for moving the arm using the invers kinematics algorithm are arm-1.ipy and AA-pro.urdf. You set the var target_position to the position you want the robot arm to end up at



presentation Slides:
https://docs.google.com/presentation/d/1IhQXdfzRPZc8SzQUHTz2jPAfiCpnQxVBbVohs_bW7B8/edit?usp=sharing
