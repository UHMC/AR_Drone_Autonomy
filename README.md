# AR_Drone_Autonomy

## This repository contains code contributed by students at UH Maui College to the basic setup from the edX course "TUMx.AUTONAVx.2T2015"

### NOTICE: Follow the INITIAL SETUP procedure prior to cloning.
### See below.


## ENVIRONMENT:

Control computer OS: Ubuntu 12.04 LTS

ROS version: Fuerte


## INITIAL SETUP:

1. Install Ubuntu 12.04 LTS (link: http://releases.ubuntu.com/12.04/ )
2. Follow the instructions in ./AR_Drone_Instructions_Webpage/AR_Drone_Instructions_Wiki_edX.html  
(originally taken from https://courses.edx.org/courses/course-v1:TUMx+AUTONAVx+2T2015/wiki/TUMx.AUTONAVx.2T2014/ardrone-instructions/ )
3. Clone this repository into ~/workshop/autonavx_ardrone/ardrone_python/src/ by opening a terminal and running the following commands:  
`$ cd ~/workshop/autonavx_ardrone/ardrone_python/src/`  
`$ git clone https://github.com/UHMC/AR_Drone_Autonomy.git`

###Done!


## A DEMO QUICK-START (After INITIAL SETUP):

(Steps 6 and 7 are optional; they display real-time sensor data.)

1. Connect to the access point created by the drone
2. Open a terminal
3. `$ roscore`
4. Open another terminal
5. `$ rosrun ardrone_autonomy ardrone_driver`
6. Open another terminal
7. `$ rostopic echo /ardrone/navdata`
8. Open another terminal
9. `$ roscd ardrone_python/src/AR_Drone_Autonomy`
10. `$ python ex_takeoff_turn_land.py`

###Done! To close, go to original terminal, press `Ctrl+c`, and then close all other terminals.
