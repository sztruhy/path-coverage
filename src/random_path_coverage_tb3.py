#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist #
import random




def callback(dt):

    print '-------------------------------------------'
    print 'Range data at 0 deg:   {}'.format(dt.ranges[0])
    print 'Range data at 60 deg:  {}'.format(dt.ranges[60])
    print 'Range data at 300 deg: {}'.format(dt.ranges[300])
    print '-------------------------------------------'

    thr = 0.8 # Laser scan range threshold
    thr2 = 0

    hasObsInFront = dt.ranges[0]<=thr and dt.ranges[0] != 0.0
    hasObsOnRight = dt.ranges[60]<=thr and dt.ranges[60] != 0.0
    hasObsOnLeft = dt.ranges[300]<=thr and dt.ranges[300] != 0.0


    if not hasObsInFront and not hasObsOnLeft and not  hasObsOnRight: 		 # Checks if there are obstacles in front and
                                                                         # 15 degrees left and right (Try changing the
									 # the angle values as well as the thresholds)
        move.linear.x = 0.4 # go forward (linear velocity)
        move.angular.z = 0.0 # do not rotate (angular velocity)
    elif hasObsOnLeft: 
          move.linear.x = 0.0 # stop
	  move.angular.z = 0.8 # rotate counter-clockwise


    elif hasObsOnRight:
          move.linear.x = 0.0 # stop
	  move.angular.z = -0.8 # rotate not counter-clockwise



    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
rospy.init_node('random_path_coverage_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  # Publisher object which will publish "Twist" type messages
                            				 # on the "/cmd_vel" Topic, "queue_size" is the size of the
                                                         # outgoing message queue used for asynchronous publishing

sub = rospy.Subscriber("/scan", LaserScan, callback)  # Subscriber object which will listen "LaserScan" type messages
                                                      # from the "/scan" Topic and call the "callback" function
						      # each time it reads something from the Topic

rospy.spin() # Loops infinitely until someone stops the program execution

