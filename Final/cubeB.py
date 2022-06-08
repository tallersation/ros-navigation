from turtle import up
from sensor_msgs.msg import Image, CameraInfo
import cv2, cv_bridge, rospy, numpy
from geometry_msgs.msg import Twist


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.twist = Twist()

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = numpy.array([110,50,50])
        upper_blue = numpy.array([130,255,255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        h, w, d = image.shape
        # search_top = int(3*h/4)
        # search_bot = search_top + 20
        # mask[0:search_top, 0:w] = 0
        # mask[search_bot:h, 0:w] = 0
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image, (cx, cy), 20, (0,0,255), -1)
        
        cv2.imshow("mask", mask)
        cv2.imshow("output", image)
        cv2.waitKey(3)

follower = Follower()