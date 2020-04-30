#!/usr/bin/python

import epics
import os
import sys
import time
import math
import unittest
import ecmcSlitDemoLib

print(sys.prefix)

leftMotor = 'MEBT-EMU:Axis1'
rightMotor = 'MEBT-EMU:Axis2'

#Reset error on all axis
print 'Reset error on all axes.'
ecmcSlitDemoLib.setAxisReset(leftMotor, 1)
ecmcSlitDemoLib.setAxisReset(rightMotor, 1)
time.sleep(0.5)
ecmcSlitDemoLib.setAxisReset(leftMotor, 0)
ecmcSlitDemoLib.setAxisReset(rightMotor, 0)


#enable amplifier of left and right motor
print ('Disable amplifiers on all axes.')
ecmcSlitDemoLib.setAxisEnable(leftMotor, 1)
ecmcSlitDemoLib.setAxisEnable(rightMotor, 1)
time.sleep(1) #ensure that enabled goes down
error=ecmcSlitDemoLib.getAxisError(leftMotor,1)
error=ecmcSlitDemoLib.getAxisError(rightMotor,1)


#Start homing sequences
ecmcSlitDemoLib.triggHomeAxis(leftMotor,1)
ecmcSlitDemoLib.triggHomeAxis(rightMotor,1)

print ('Wait for homing sequences to finish:')
done=ecmcSlitDemoLib.waitForAxis(leftMotor,180)
if not done:
  print '%s failed to home.' % leftMotor
  sys.exit()

done=ecmcSlitDemoLib.waitForAxis(rightMotor,180)
if not done:
  print ("%s failed to home.") % rightMotor
  sys.exit()

print ('Move axis 1 to pos 40.')
done=ecmcSlitDemoLib.moveAxisPosition(leftMotor,40,100)
if not done:
  print ('%s failed to position.') % leftMotor
  sys.exit()

print ('Move axis 1 to pos 40.')
done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,40,100)
if not done:
  print ('%s failed to position.')   % rightMotor
  sys.exit()


print ('Move axis 1 to LLS.')
done=ecmcSlitDemoLib.moveAxisPosition(leftMotor,-100,100)
if not done:
  print ('%s failed to position.')   % leftMotor
  sys.exit()

print ('Move axis 2 to LLS.')
done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,-100,100)
if not done:
  print ("%s failed to position.")   % rightMotor
  sys.exit()


#disable amplifier of left and right motor
print ('Disable amplifiers on all axes.')
ecmcSlitDemoLib.setAxisEnable(leftMotor, 0)
ecmcSlitDemoLib.setAxisEnable(rightMotor, 0)
time.sleep(1) #ensure that enabled goes down
error=ecmcSlitDemoLib.getAxisError(leftMotor,1)
error=ecmcSlitDemoLib.getAxisError(rightMotor,1)

print ('The EMU axes are on the LLS position!')
print ('Now the collision avoidance system can run!')
