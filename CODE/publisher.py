#! /usr/bin/python3
import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("GOURI_pubnode",anonymous=True)
    pub=rospy.Publisher("Greetings",String,queue_size=10)
    rate=rospy.Rate(10)
    rospy.loginfo("")

    while not rospy.is_shutdown():
        msg=String()
        msg.data="Hello, I am GOURI"
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()
        
if __name__ =="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass