#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

pub = None

def imuCallback(data):
    imuData = Imu()
    imuData.header.stamp = rospy.Time.now()
    imuData.header.frame_id = 'imu_link'
    imuData.orientation = data.orientation
    imuData.orientation_covariance = data.orientation_covariance
    imuData.angular_velocity = data.angular_velocity
    imuData.angular_velocity_covariance = data.angular_velocity_covariance
    imuData.linear_acceleration = data.linear_acceleration
    imuData.linear_acceleration_covariance = data.linear_acceleration_covariance
    pub.publish(imuData)


def imuListener():
    global pub
    rospy.init_node('trekking_imu_node')

    pub = rospy.Publisher('/trekking/imu', Imu, queue_size=10)

    rospy.Subscriber('/imu', Imu, imuCallback)

    rospy.spin()

if __name__ == '__main__':
    imuListener()
