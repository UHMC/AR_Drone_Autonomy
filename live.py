#!/usr/bin/env python

#modified from example3_trajectory.py

#usage:
# $ python
# >>> import live
# >>> live.init()
# >>> live.<commandName>()
# etc.

import rospy
import roslib; roslib.load_manifest('ardrone_python')
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3

#rospy.init_node('example_node', anonymous=True)
    
# publish commands (send to quadrotor)
pub_velocity = rospy.Publisher('/cmd_vel', Twist)
pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty)
pub_land = rospy.Publisher('/ardrone/land', Empty)
pub_reset = rospy.Publisher('/ardrone/reset', Empty)

def init():
	rospy.init_node('example_node', anonymous=True)
    
def toff():
	print("takeoff..")
	pub_takeoff.publish(Empty())

def rotl():
    	print("turning left around yaw axis..")
    	pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,1)))
    
def rotr():
	print("turning right around yaw axis..")
	pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,-1)))

def hov():
	print("hover..")
    	pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))

def land():
	print("land..")
	pub_land.publish(Empty())

def help():
	print("toff(): take off\n hov(): hover \n rotl(): rotate left \n rotr(): rotate right \n land(): land")

#if __name__=='__main__'):
#	print("ready!")
