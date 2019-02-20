#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace

def callback(scan):
    pub_topic = rospy.get_param("/open_space_publisher/pub_topic")
    pub = rospy.Publisher(pub_topic, OpenSpace, queue_size=10)
    open_space = OpenSpace()
    open_space.distance = scan.ranges[0] 
    open_space.angle = scan.angle_min
    for i in range(1, len(scan.ranges)):
        if scan.ranges[i] > open_space.distance:
            open_space.distance = scan.ranges[i]
            open_space.angle = scan.angle_min + scan.angle_increment*i
    rospy.loginfo(open_space)
    pub.publish(open_space)


def listener():
    sub_topic = rospy.get_param("/open_space_publisher/sub_topic")
    rospy.Subscriber(sub_topic, LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('open_space_publisher', anonymous=True)
    listener()
