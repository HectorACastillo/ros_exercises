import rospy
from std_msgs.msg import Float32
import math

def callback(data):
    pub = rospy.Publisher('random_float_log', Float32, queue_size=10)
    log_of_float = Float32(math.log(data.data))
    rospy.loginfo(log_of_float)
    pub.publish(log_of_float)


def listener():
    rospy.init_node('simple_subscriber', anonymous=True)
    rospy.Subscriber("my_random_float", Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
