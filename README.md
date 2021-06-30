# # path-coverage
This is simple obstacle avoidance path covrage algorithm for my thesis with a Turtlebot3 using ROS.
This was tested on a real Turtlebot3 Burger with Ubuntu 16.04 LTS

## How to install it
```
cd ~/catkin_ws/src
git clone https://github.com/sztruhy/path-coverage.git
cd ~/catkin_ws
catkin_make
```

## How to run it
```
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch path-coverage random_path_coverage.launch
```



## Details
If you got some Error about the "random_path_covrage_tb3.py" just make this file executeable in the properties of the file and it should be fine.
In the slc folder you can find the simple python code with comments.

If you run roselaunch 'path-coverage laser.launch' you can see real time the data about the disctances at a specific degree which are set in the code.
For us the 'float32[]' is the importent that you can see if you run 'rostopic type /scan | show rosmsg show. this message is a list of 359 distance values around the robot in every degree.

'rostopic echo cmd_vel' is where we can see the real time data for the linear and angular values.

'rostopic type /odom | rosmsg show' is where we can see the linear and angular values.




## Reference
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview
