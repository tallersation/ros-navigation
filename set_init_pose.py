#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

rospy.init_node('set_init_pose', anonymous=True)
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)

initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map"
initpose_msg.pose.pose.position.x = -2.25
initpose_msg.pose.pose.position.y = -0.04
initpose_msg.pose.pose.position.z = 0.00
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = 0.0
initpose_msg.pose.pose.orientation.w = 1

rate = rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(initpose_msg)
    rate.sleep()