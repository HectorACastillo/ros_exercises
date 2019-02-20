import rospy
from sensor_msgs.msg import LaserScan
from random import *
import math

def scanner():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher', anonymous=True)
    rate = rospy.Rate(20) # 20 hz
    while not rospy.is_shutdown():
        scan = LaserScan()
        scan.header.stamp = rospy.Time.now()
        scan.header.frame_id = "base_link"
        scan.angle_min = -(2.0/3.0)*math.pi
        scan.angle_max = (2.0/3.0)*math.pi
        scan.angle_increment = (1/300.0)*math.pi
        scan.scan_time = 0.05
        scan.range_min = 1.0
        scan.range_max = 10.0
        for i in range(int((scan.angle_max-scan.angle_min)/scan.angle_increment + 1)):
            scan.ranges.append(uniform(scan.range_min, scan.range_max))
        rospy.loginfo(scan)
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        scanner()
    except rospy.ROSInterruptException:
        pass
