#!/usr/bin/env python

import epics
import os
import sys
import time
import math
import unittest
import ecmcSlitDemoLib

leftMotor = 'MEBT-EMU:Axis1'
rightMotor = 'MEBT-EMU:Axis2'

#Reset error on all axis
print 'Reset error on all axes.'
ecmcSlitDemoLib.setAxisReset(leftMotor, 1)
ecmcSlitDemoLib.setAxisReset(rightMotor, 1)
time.sleep(0.5)
ecmcSlitDemoLib.setAxisReset(leftMotor, 0)
ecmcSlitDemoLib.setAxisReset(rightMotor, 0)

#ensure of all axis are enable 
print 'Enable Axes'
ecmcSlitDemoLib.setAxisEnable(leftMotor, 1)
ecmcSlitDemoLib.setAxisEnable(rightMotor, 1)
time.sleep(0.5) #ensure that axes are enabled 
error=ecmcSlitDemoLib.getAxisError(leftMotor,1)
error=ecmcSlitDemoLib.getAxisError(rightMotor,1);


Step = 1
while Step==1:
 if Step==1:
  LLS1 = int(epics.caget(leftMotor + '.LLS'))
  LLS2 = int(epics.caget(rightMotor + '.LLS'))
  print'LLS1 %d LLS2 %d' %(LLS1,LLS2)
  if LLS1 and LLS2:
    print 'Both axes are in the LLS'
    Step = 2
  elif LLS1 or LLS2:
    print 'One of the Axes is in the LLS position'
    Step = 3
  else:
    print 'Axes are not in place'
    Step = 4
 if Step==2:
  #run right Motor to pos 10
  print 'Move right axis to pos 10'
  done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,10,10)
  if not done:
    print "%s failed to position." % rightMotor
    sys.exit()

  time.sleep(10)
  #run right Motor to pos 0
  print 'Move right axis to pos 0'
  done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,-10,10)
  if not done:
    print "%s failed to position." % rightMotor
    sys.exit()
    time.sleep(10)
  Step=1  
 if Step==3:
  if LLS1 and not LLS2:
    print 'Axis 1 is in the LLS position.\n'
    print 'Move the axis 2\n'
    done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,10,10)
    if not done:
      print "%s failed to position." % rightMotor
      sys.exit()
  
  time.sleep(10)
  #run right Motor to pos 0
  print 'Move right axis to pos 0'
  done=ecmcSlitDemoLib.moveAxisPosition(rightMotor,-10,10)
  if not done:
    print "%s failed to position." % rightMotor
    sys.exit()
  time.sleep(10)
  if LLS2 and not LLS1:      
    print 'Axis 1 is in the LLS position.\n'
    print 'Move the axis 2\n'
    done=ecmcSlitDemoLib.moveAxisPosition(leftMotor,10,10)
    if not done:
      print "%s failed to position." % leftMotor
      sys.exit()
  time.sleep(10)
  #run right Motor to pos 0
  print 'Move right axis to pos 0'
  done=ecmcSlitDemoLib.moveAxisPosition(leftMotor,-10,10)
  if not done:
    print "%s failed to position." % leftMotor
    sys.exit()
  time.sleep(10)
  Step=1
  
 
