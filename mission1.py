
import rospy
from turtlesim.msg import Pose

def sub_callback(data):
    rospy.loginfo(data)


if __name__ == '__main__':
    rospy.init_node("deneme_sub")

    sub = rospy.Subscriber("/turtle1/pose", Pose , callback=sub_callback)

    rospy.spin()