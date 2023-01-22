import math
import rospy
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose 
from math import sqrt , atan2



class MyClass:

    velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    x0 = 0
    y0 = 0
    yaw = 0
    
    def _init_(self):
        pass
        #self.x0 = 0
        #self.y0 = 0
        #self.velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        

    def poseCallback(self,pose_message):

        self.x0 = pose_message.x
        self.y0 = pose_message.y
        self.yaw = pose_message.theta
        #print(self.x0, "pose içindeki x0 calisiyo ")
        


    def go_to_goal(self, x_goal, y_goal):

        self.velocity_message = Twist()

        #print(x_goal, "habu gotogoal x_goal calisiyo ")
        #print(y_goal, "habu gotogoal y_goal calisiyo ")


        K_linear = 0.5
        distance = abs( math.sqrt(((x_goal-self.x0)**2)+ ((y_goal-self.y0)**2)))
        self.linear_speed = distance*K_linear

        K_angular = 4
        desired_angular_goal = math.atan2(y_goal-self.y0, x_goal-self.x0)
        self.angular_speed = (desired_angular_goal-self.yaw)*K_angular

        self.velocity_message.linear.x = self.linear_speed
        self.velocity_message.angular.z = self.angular_speed

        #print(self.x0, "hangi deger bu")
        print ('x=' , self.x0, 'y=' , self.y0, 'distance to goal= ' ,distance)


        if (distance > 0.1):
            self.velocity_publisher.publish(self.velocity_message)
    
               

if __name__ == '__main__':
    try:
        rospy.init_node("pose")
        rate = rospy.Rate(3)
        obje = MyClass()
        while not rospy.is_shutdown():
            pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback=obje.poseCallback)
            obje.go_to_goal(11,2)
            rate.sleep()
        
    except rospy.ROSInterruptException:
        rospy.loginfo("node has been terminated")

    

    
