#! /usr/bin/python3
import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(f"recieved: {msg.data}")

def publisher():
    rospy.init_node("GOURI")
    pub=rospy.Publisher("hello_class",String,queue_size=10)
    sub=rospy.Subscriber("Welcome",String,callback=call_back)
    rate=rospy.Rate(10)
    rospy.loginfo("")

    while not rospy.is_shutdown():
        txt="HELLO RAA24_26"
        msg=String()
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()
        
if __name__ =="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass