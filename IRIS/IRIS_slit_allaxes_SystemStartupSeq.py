#!/usr/bin/env python

import epics
import os
import sys
import time
import math
import unittest
import ecmcSlitDemoLib

P = 'LEBT-010:ID-Iris:'
Mtr1 = P+'Axis:Mtr1'
Mtr2 = P+'Axis:Mtr2'
Mtr3 = P+'Axis:Mtr3'
Mtr4 = P+'Axis:Mtr4'
Mtr5 = P+'Axis:Mtr5'
Mtr6 = P+'Axis:Mtr6'

gapMotor = P+'slit_gap'
centerMotor = P+'slit_center'
HomProcLeft = 2
HomProcRight = 1

#Reset error on all axis
print 'Reset error on all axes.'
ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)
time.sleep(0.5)
ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)

#disable axes
print 'Disable all axes'
ecmcSlitDemoLib.setAxisEnable(Mtr1, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr2, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr3, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr4, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr5, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr6, 0)
ecmcSlitDemoLib.setAxisEnable(gapMotor, 0)
ecmcSlitDemoLib.setAxisEnable(centerMotor, 0)

print 'Ensure enable goes down'
time.sleep(0.5) #ensure that enabled goes down
error=ecmcSlitDemoLib.getAxisError(Mtr1,1)
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
error=ecmcSlitDemoLib.getAxisError(Mtr3,1)
error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
error=ecmcSlitDemoLib.getAxisError(Mtr5,1)
error=ecmcSlitDemoLib.getAxisError(Mtr6,1);
error=ecmcSlitDemoLib.getAxisError(gapMotor,1)
error=ecmcSlitDemoLib.getAxisError(centerMotor,1);

#set internal traj source of all axis 
print 'Set internal trajectory source on all axes'
epics.caput(centerMotor + '-TrajSourceType-Cmd', 0)
epics.caput(gapMotor + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr1 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr2 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr3 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr4 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr5 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr6 + '-TrajSourceType-Cmd', 0)

print 'Ensure internal trajectory source on all axes'
error=ecmcSlitDemoLib.getAxisError(Mtr1,1);
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
error=ecmcSlitDemoLib.getAxisError(Mtr3,1);
error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
error=ecmcSlitDemoLib.getAxisError(Mtr5,1);
error=ecmcSlitDemoLib.getAxisError(Mtr6,1);
error=ecmcSlitDemoLib.getAxisError(gapMotor,1);
error=ecmcSlitDemoLib.getAxisError(centerMotor,1);

print 'Start homing sequence'
#Start homing sequences
ecmcSlitDemoLib.triggHomeAxis(Mtr1,HomProcLeft)
ecmcSlitDemoLib.triggHomeAxis(Mtr2,HomProcLeft)
ecmcSlitDemoLib.triggHomeAxis(Mtr3,HomProcRight)
ecmcSlitDemoLib.triggHomeAxis(Mtr4,HomProcRight)
ecmcSlitDemoLib.triggHomeAxis(Mtr5,HomProcRight)
ecmcSlitDemoLib.triggHomeAxis(Mtr6,HomProcLeft)


print 'Wait for homing sequences to finish:'
done=ecmcSlitDemoLib.waitForAxis(Mtr1,1800)
if not done:
  print "%s failed to home." % leftMotor
  sys.exit()
done=ecmcSlitDemoLib.waitForAxis(Mtr2,1800)
if not done:
  print "%s failed to home." % rightMotor
  sys.exit()
print 'Wait for homing sequences to finish:'
done=ecmcSlitDemoLib.waitForAxis(Mtr3,1800)
if not done:
  print "%s failed to home." % leftMotor
  sys.exit()
done=ecmcSlitDemoLib.waitForAxis(Mtr4,1800)
if not done:
  print "%s failed to home." % rightMotor
  sys.exit()
print 'Wait for homing sequences to finish:'
done=ecmcSlitDemoLib.waitForAxis(Mtr5,1800)
if not done:
  print "%s failed to home." % leftMotor
  sys.exit()
done=ecmcSlitDemoLib.waitForAxis(Mtr6,1800)
if not done:
  print "%s failed to home." % rightMotor
  sys.exit()

#disable amplifiers
print 'Disable amplifiers on all axes.'
ecmcSlitDemoLib.setAxisEnable(Mtr1, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr2, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr3, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr4, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr5, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr6, 0)
ecmcSlitDemoLib.setAxisEnable(gapMotor, 0)
ecmcSlitDemoLib.setAxisEnable(centerMotor, 0)

time.sleep(1) #ensure that enabled goes down
error=ecmcSlitDemoLib.getAxisError(Mtr1,1);
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
error=ecmcSlitDemoLib.getAxisError(Mtr3,1);
error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
error=ecmcSlitDemoLib.getAxisError(Mtr5,1);
error=ecmcSlitDemoLib.getAxisError(Mtr6,1);
error=ecmcSlitDemoLib.getAxisError(gapMotor,1);
error=ecmcSlitDemoLib.getAxisError(centerMotor,1);

#change traj source of left and right motor to external
print 'Set traj source to external for left and right axis.'
epics.caput(Mtr1 + '-TrajSourceType-Cmd', 1)
epics.caput(Mtr2 + '-TrajSourceType-Cmd', 1)
epics.caput(Mtr3 + '-TrajSourceType-Cmd', 1)
epics.caput(Mtr4 + '-TrajSourceType-Cmd', 1)
epics.caput(Mtr5 + '-TrajSourceType-Cmd', 1)
epics.caput(Mtr6 + '-TrajSourceType-Cmd', 1)

print 'Ensure external trajectory source on all axes'
error=ecmcSlitDemoLib.getAxisError(Mtr1,1);
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
error=ecmcSlitDemoLib.getAxisError(Mtr3,1);
error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
error=ecmcSlitDemoLib.getAxisError(Mtr5,1);
error=ecmcSlitDemoLib.getAxisError(Mtr6,1);


time.sleep(5) #ensure that enabled goes up


#enable gap and center motor
print 'Enable amplifiers on centre and gap axis.'
epics.caput(gapMotor + '.CNEN', 1)
epics.caput(centerMotor + '.CNEN', 1)
time.sleep(1) #ensure that enabled goes up
error=ecmcSlitDemoLib.getAxisError(gapMotor,1)
error=ecmcSlitDemoLib.getAxisError(centerMotor,1)

#enable left and right blades
print 'Enable amplifiers for real axes.'
epics.caput(Mtr1 + '.CNEN', 1)
epics.caput(Mtr2 + '.CNEN', 1)
epics.caput(Mtr3 + '.CNEN', 1)
epics.caput(Mtr4 + '.CNEN', 1)
epics.caput(Mtr5 + '.CNEN', 1)
epics.caput(Mtr6 + '.CNEN', 1)
time.sleep(1) #ensure that enabled goes up
error=ecmcSlitDemoLib.getAxisError(Mtr1,1)
error=ecmcSlitDemoLib.getAxisError(Mtr2,1)
error=ecmcSlitDemoLib.getAxisError(Mtr3,1)
error=ecmcSlitDemoLib.getAxisError(Mtr4,1)
error=ecmcSlitDemoLib.getAxisError(Mtr5,1)
error=ecmcSlitDemoLib.getAxisError(Mtr6,1)

print "Slit system ready to operate!"


