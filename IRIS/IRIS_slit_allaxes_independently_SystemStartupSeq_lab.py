#!/usr/bin/env python

import epics
import os
import sys
import time
import math
import unittest
import ecmcSlitDemoLib

P = 'TestIris-MCU1026:Ctrl-ECAT-1:'
Mtr1 = P+'Axis1'
Mtr2 = P+'Axis2'
#Mtr3 = P+'Axis3'
#Mtr4 = P+'Axis4'
#Mtr5 = P+'Axis5'
#Mtr6 = P+'Axis6'

gapMotor = P+'slit_gap'
centerMotor = P+'slit_center'
HomProcLeft = 2
HomProcRight = 1

#Reset error on all axis
print 'Reset error on all axes.'
ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)
time.sleep(0.5)
ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)

#ensure internal traj source of all axis 
print 'Ensure internal trajectory source on all axes'
ecmcSlitDemoLib.setAxisEnable(Mtr1, 0)
ecmcSlitDemoLib.setAxisEnable(Mtr2, 0)
#ecmcSlitDemoLib.setAxisEnable(Mtr3, 0)
#ecmcSlitDemoLib.setAxisEnable(Mtr4, 0)
#ecmcSlitDemoLib.setAxisEnable(Mtr5, 0)
#ecmcSlitDemoLib.setAxisEnable(Mtr6, 0)
ecmcSlitDemoLib.setAxisEnable(gapMotor, 0)
ecmcSlitDemoLib.setAxisEnable(centerMotor, 0)

print 'Ensure enable goes down'
time.sleep(0.5) #ensure that enabled goes down
error=ecmcSlitDemoLib.getAxisError(Mtr1,1)
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr3,1)
#error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr5,1)
#error=ecmcSlitDemoLib.getAxisError(Mtr6,1);
error=ecmcSlitDemoLib.getAxisError(gapMotor,1)
error=ecmcSlitDemoLib.getAxisError(centerMotor,1);

#epics.caput(centerMotor + '-TrajSourceType-Cmd', 0)
#epics.caput(gapMotor + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr1 + '-TrajSourceType-Cmd', 0)
epics.caput(Mtr2 + '-TrajSourceType-Cmd', 0)
#epics.caput(Mtr3 + '-TrajSourceType-Cmd', 0)
#epics.caput(Mtr4 + '-TrajSourceType-Cmd', 0)
#epics.caput(Mtr5 + '-TrajSourceType-Cmd', 0)
#epics.caput(Mtr6 + '-TrajSourceType-Cmd', 0)

error=ecmcSlitDemoLib.getAxisError(Mtr1,1);
error=ecmcSlitDemoLib.getAxisError(Mtr2,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr3,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr4,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr5,1);
#error=ecmcSlitDemoLib.getAxisError(Mtr6,1);
error=ecmcSlitDemoLib.getAxisError(gapMotor,1);
error=ecmcSlitDemoLib.getAxisError(centerMotor,1);

print 'Ensure enable goes down'

#Start homing sequences
ecmcSlitDemoLib.triggHomeAxis(Mtr1,HomProcLeft)
ecmcSlitDemoLib.triggHomeAxis(Mtr2,HomProcRight)
#ecmcSlitDemoLib.triggHomeAxis(Mtr3,HomProcLeft)
#ecmcSlitDemoLib.triggHomeAxis(Mtr4,HomProcLeft)
#ecmcSlitDemoLib.triggHomeAxis(Mtr5,HomProcLeft)
#ecmcSlitDemoLib.triggHomeAxis(Mtr6,HomProcRight)


print 'Wait for homing sequences to finish:'
done=ecmcSlitDemoLib.waitForAxis(Mtr1,1800)
if not done:
  print "%s failed to home." % leftMotor
  sys.exit()
done=ecmcSlitDemoLib.waitForAxis(Mtr2,1800)
if not done:
  print "%s failed to home." % rightMotor
  sys.exit()
#print 'Wait for homing sequences to finish:'
#done=ecmcSlitDemoLib.waitForAxis(Mtr3,1800)
#if not done:
#  print "%s failed to home." % leftMotor
#  sys.exit()
#done=ecmcSlitDemoLib.waitForAxis(Mtr4,1800)
#if not done:
#  print "%s failed to home." % rightMotor
#  sys.exit()
#print 'Wait for homing sequences to finish:'
#done=ecmcSlitDemoLib.waitForAxis(Mtr5,1800)
#if not done:
#  print "%s failed to home." % leftMotor
#  sys.exit()
#done=ecmcSlitDemoLib.waitForAxis(Mtr6,1800)
#if not done:
#  print "%s failed to home." % rightMotor
#  sys.exit()


print 'The IRIS is ready to move: you can move 6 axes independentlyc'
