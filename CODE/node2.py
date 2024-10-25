#! /usr/bin/python3
import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("M1RAA 2024")
    pub1=rospy.Publisher("Welcome",String,queue_size=10)
    pub2=rospy.Publisher("hello_college",String,queue_size=10)
    sub=rospy.Subscriber('hello_class',String)
    rate=rospy.Rate(10)
    rospy.loginfo("")

    while not rospy.is_shutdown():
        msg1=String()
        msg2=String()
        msg1.data="Hello Gouri Welcome!"
        msg2.data="Hello CET!"
        pub1.publish(msg1)
        pub2.publish(msg2)
        rospy.loginfo(msg1.data)
        rospy.loginfo(msg2.data)
        rate.sleep()
        
if __name__ =="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass