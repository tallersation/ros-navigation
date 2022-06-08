#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import os

from cubeY import Follower
#Callback definition

def active_cb(extra):
	rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
	rospy.loginfo("Current locationb: " + str(feedback))

def done_cb(status, result):
	if status == 3:
		rospy.loginfo("Goal reached")
	if status == 2 or status == 8:
		rospy.loginfo("Goal calcelled")
	if status == 4:
		rospy.loginfo("Goal aborted")

rospy.init_node("send_goal")
follower = Follower()
navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()

#Example of navigation goal

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

goal.target_pose.pose.position.x = -1.05
goal.target_pose.pose.position.y = -1.70
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.w = 1
goal.target_pose.pose.orientation.z = -1.1

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finish = navclient.wait_for_result()

goal.target_pose.pose.position.x = 0.20
goal.target_pose.pose.position.y = -1.58
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.w = -0.35
goal.target_pose.pose.orientation.z = -0.35

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finish = navclient.wait_for_result()

goal.target_pose.pose.position.x = 0.49
goal.target_pose.pose.position.y = -0.65
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.w = 1.55
goal.target_pose.pose.orientation.z = 1.55

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finish = navclient.wait_for_result()

if not finish:
	rospy.logerr("Action server not available")
else:
	rospy.loginfo( navclient.get_result())
	os.system('python3 moveit2.py && python3 send_goal1-1.py')