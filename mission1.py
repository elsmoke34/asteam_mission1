
import rospy
from ros_essentials_cpp.msg import MyVelocity
from turtlesim.msg import Pose

def pose_callback(pose):
    cmd = MyVelocity()
    cmd.vel_x = pose.linear_velocity
    cmd.vel_y = pose.linear_velocity
    cmd.ang_z = pose.theta
    pub.publish(cmd)
    print("X Doğrultusunda Lİneer Hizi:",cmd.vel_x,'\n',"Y Doğrultusunda Lİneer Hizi:",cmd.vel_y,'\n',"Baktiği Yön:", cmd.ang_z)


if __name__ == '__main__':
    rospy.init_node('mission1_node')
    pub = rospy.Publisher('mission1_topic', MyVelocity , queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose , callback=pose_callback)
    rospy.loginfo("Node has been started.")

    rospy.spin()
