#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from random import *
import math

def scanner():
    pub_topic = rospy.get_param("/fake_scan_publisher/pub_topic")
    pub = rospy.Publisher(pub_topic, LaserScan, queue_size=10)
    pub_rate = rospy.get_param("/fake_scan_publisher/pub_rate")
    rate = rospy.Rate(pub_rate) # default 20 hz
    while not rospy.is_shutdown():
        scan = LaserScan()
        scan.header.stamp = rospy.Time.now()
        scan.header.frame_id = "base_link"
        scan.angle_min = rospy.get_param("/fake_scan_publisher/angle_min") # -(2.0/3.0)*math.pi
        scan.angle_max = rospy.get_param("/fake_scan_publisher/angle_max") # (2.0/3.0)*math.pi
        scan.angle_increment = rospy.get_param("/fake_scan_publisher/angle_increment") # (1/300.0)*math.pi
        scan.scan_time = 0.05
        scan.range_min = rospy.get_param("/fake_scan_publisher/range_min") # 1.0
        scan.range_max = rospy.get_param("/fake_scan_publisher/range_max") # 10.0
        for i in range(int((scan.angle_max-scan.angle_min)/scan.angle_increment + 1)):
            scan.ranges.append(uniform(scan.range_min, scan.range_max))
        rospy.loginfo(scan)
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('fake_scan_publisher', anonymous=True)
        scanner()
    except rospy.ROSInterruptException:
        pass
