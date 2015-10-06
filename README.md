# Turtlesim: Publisher/Subcriber Program

 ##Task: 
 Create a publisher node to publish a desired trajectory over the cmd_vel topic to the subscriber turtlesim

package.xml is updated with the appropriate dependencies

## Launch File
Launch the sim with the following command:

	$roslaunch tutle_hw1 turtle_launch.xml T_tur:= "value"

The T_tur argument allows the user to input the desired period over which the turtlesim will complete the Figure 8 trajectory. Replace "value" with the desied time for one loop in seconds.

If T_tur argument is not specified the simulation defauls to a period of T_tur:=8

##The Node

### Set Starting Position
The turtlesim is relocated to the center of the simulation using TeleportAbsolute

### Define the Kinematics
This node must publish linear and angular velocity commands to the turtlesim node. Required parameters are calculated in the equations() function. Given the desired trajectory equations, the linear velocity and acceleration  equations are determined by taking the first and second derivative respectively.The cmd_vel topic takes forward linear velocity and angular velocity information, which is derived from the linear velocity and acceleration componenets.

### cmd_vel Topic
The cmd_vel node and publisher are initialized. Twist() is initialized with zeros, rospy.Rate is set to 60 Hz, and the starting time determined

While the program is running, the current time is determined and the equations() function is called to calculate the linear and angular velocity of the turtle for that time step. The calcuated values are published to Twist()

## Bagfiles
A bagfile directory is created and a bagfile recorded. The length of the bagfile is determined based on the rospy.Rate and the period. For this example the the period is set to T_tur:=15. Given a frequency of 60Hz, the turtle requires 15*60 = 900 messages for a full-cycle recording. 1000 msgs are stored.

	$rosbag record -l 1000 /turtle1/cmd_vel 

