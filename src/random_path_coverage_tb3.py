#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan 						# LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist #
#import random




def callback(dt):								

    print '__'
    print 'Front range (0 degree):   {}'.format(dt.ranges[0])			 # Printing out live data about the robot 
    print 'Right range (60 degree):  {}'.format(dt.ranges[60])			 # scanning the front,left and right.
    print 'Left range (300 degree):  {}'.format(dt.ranges[300])			 #Formating them for the print.

    thr = 0.4 									 # Distance value for how close can get the robot to an object

    hasObsInFront = dt.ranges[0]<=thr and dt.ranges[0] != 0.0			 # Checks if the robot has obstacles in front of it
    hasObsOnRight = dt.ranges[60]<=thr and dt.ranges[60] != 0.0			 # Checks if the robot has obstacles on the right side of it at 60 degree
    hasObsOnLeft = dt.ranges[300]<=thr and dt.ranges[300] != 0.0		 # Checks if the robot has obstacles on the left side of it at 300 degree
										 #!= 0.0 is there because in real life if something is too far the lidar shows 0.0


    if not hasObsInFront and not hasObsOnLeft and not  hasObsOnRight: 		 # Checking for obstacle in front of the robot
                                                                                 # The degrees are set at this point.

        move.linear.x = 0.05 							 # Setting the foward speed if the path is clear at the front
        move.angular.z = 0.0 							 # Left and right velocity is 0
    elif hasObsOnLeft: 
          move.linear.x = 0.0 							 # Stopping the linear velocity
	  move.angular.z = 0.8 							 # Rotating the robot to the right


    elif hasObsOnRight:
          move.linear.x = 0.0 							 # Stopping the linear velocity
	  move.angular.z = -0.8 						 # Rotating the robot to the left

    pub.publish(move) 								 # publish the move object


move = Twist()									 # Creates a Twist message type object
rospy.init_node('random_path_coverage_node') 					 # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  			 # Publisher object which will publish "Twist" type messages
                            							 # on the "/cmd_vel" Topic, "queue_size" is the size of the
                                                         			 # outgoing message queue used for asynchronous publishing

sub = rospy.Subscriber("/scan", LaserScan, callback) 				 # Subscriber object which will listen "LaserScan" type messages
                                                     				 # from the "/scan" Topic and call the "callback" function
						      				 # each time it reads something from the Topic
rospy.spin() 									 # Loops infinitely until someone stops the program execution

