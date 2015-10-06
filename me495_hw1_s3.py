#!/usr/bin/env python

import rospy
import numpy
import rosbag
import math
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

#set turtle starting position
rospy.wait_for_service('turtle1/teleport_absolute')
start_pos = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
start_pos(5.4, 5.4, 0.0)

#total time: sinusoid period 
Tn = rospy.get_param('~/Garry/T_tur')

def equations(tn,T):
	#current time
	t = tn

	#tradjectory equations	
	#x = 3*math.sin(4*math.pi*t/T)
	#y = 3*math.sin(2*pi*t/T)]

	#velocity equations
	x_prime = 12*math.pi*math.cos(4*math.pi*t/T)/T
	y_prime = 6*math.pi*math.cos(2*math.pi*t/T)/T

	#acceleration equation
	x_dblPrime = -48*math.pi**2*math.sin(4*math.pi*t/T)/(T**2)
	y_dblPrime = -12*math.pi**2*math.sin(2*math.pi*t/T)/(T**2)

	#turtle parameters: forward linear velocity, angular velocity
	v_turtle = math.sqrt(x_prime**2+y_prime**2)
	omega_turtle = (y_dblPrime*x_prime-x_dblPrime*y_prime)/(x_prime**2+y_prime**2) # REFERENCE!!!!!

	return [v_turtle, omega_turtle]

def set_cmd_vel():
	#initialize node
	rospy.init_node('set_cmd_vel', anonymous=True)

	#initialize publisher
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

	#set frequency
	r = rospy.Rate(60)

	#publish to topic
	ti = rospy.get_time() #starting tine

	#initialize Twist
	cmd_vel_value = Twist()

	while not rospy.is_shutdown():

		now = rospy.get_time()-ti #current time

		v_tur = equations(now,Tn)[0]
		w_tur = equations(now, Tn)[1]

		cmd_vel_value.linear.x = v_tur
		cmd_vel_value.angular.z = w_tur


		rospy.loginfo(cmd_vel_value)
		pub.publish(cmd_vel_value)

		r.sleep()


if __name__ == '__main__':

	try:
		set_cmd_vel()
	except rospy.ROSInterruptException: pass