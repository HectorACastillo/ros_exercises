import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

def callback(scan):
    pub_dist = rospy.Publisher('open_space/distance', Float32, queue_size=10)
    pub_angle = rospy.Publisher('open_space/angle', Float32, queue_size=10)
    
    longest = scan.ranges[0] 
    angle = scan.angle_min
    for i in range(1, len(scan.ranges)):
        if scan.ranges[i] > longest:
            longest = scan.ranges[i]
            angle = scan.angle_min + scan.angle_increment*i
    rospy.loginfo(longest)
    rospy.loginfo(angle)
    pub_dist.publish(longest)
    pub_angle.publish(angle)


def listener():
    rospy.init_node('open_space_publisher', anonymous=True)
    rospy.Subscriber("fake_scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
