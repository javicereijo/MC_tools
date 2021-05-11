#!/usr/bin/env python

import epics
import os
import sys
import time
import math
import unittest
import ecmcSlitDemoLib

P = ' TestIris-MCU1026:Ctrl-ECAT-1:'
Mtr1 = P+'Axis1'
Mtr2 = P+'Axis2'
#Mtr3 = P+'Axis:Mtr3'
#Mtr4 = P+'Axis:Mtr4'
#Mtr5 = P+'Axis:Mtr5'
#Mtr6 = P+'Axis:Mtr6'

gapMotor = P+'slit_gap'
centerMotor = P+'slit_center'


ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
#ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)
time.sleep(0.5)



while True:
    mov=10
    if mov == 10:
      print "Moving gap to %s" % mov
      done=ecmcSlitDemoLib.moveAxisPosition(gapMotor,mov)
      if not done:
        print "%s failed to position." % gapMotor
        sys.exit()
      done=ecmcSlitDemoLib.waitForAxis(gapMotor,1800)
      if not done:
        print "%s failed waiting" % gapMotor
        sys.exit() 
      mov=60
      time.sleep(2)
    if mov == 60:
      print "Moving gap to %s" % mov
      done=ecmcSlitDemoLib.moveAxisPosition(gapMotor,mov)
      if not done:
        print "%s failed to position" % gapMotor
        sys.exit()   
      done=ecmcSlitDemoLib.waitForAxis(gapMotor,1800)
      if not done:
        print "%s failed waiting" % gapMotor
        sys.exit()  
      time.sleep(2)
      #mov=0 

