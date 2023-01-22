#Turtlesim’in doğrusal hızını kontrol eden bir node yazınız

import rospy
from geometry_msgs.msg import Twist


def velocity(vel_x, vel_y):
    rospy.init_node("deneme")
    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(0.1)

    vel = Twist()

    while not rospy.is_shutdown():

        vel.linear.x = vel_x
        vel.linear.y = vel_y
        
        pub.publish(vel)
        rate.sleep()




if __name__ == '__main__':
    try:
        velocity(1,3)
    except rospy.ROSInterruptException:
        pass
   

   