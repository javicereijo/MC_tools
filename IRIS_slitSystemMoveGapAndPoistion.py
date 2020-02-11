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


ecmcSlitDemoLib.setAxisReset(Mtr1, 1)
ecmcSlitDemoLib.setAxisReset(Mtr2, 1)
ecmcSlitDemoLib.setAxisReset(Mtr3, 1)
ecmcSlitDemoLib.setAxisReset(Mtr4, 1)
ecmcSlitDemoLib.setAxisReset(Mtr5, 1)
ecmcSlitDemoLib.setAxisReset(Mtr6, 1)
ecmcSlitDemoLib.setAxisReset(gapMotor, 1)
ecmcSlitDemoLib.setAxisReset(centerMotor, 1)
time.sleep(0.5)



while True:
    mov=0
    if mov == 0:
      print "Moving gap to %s" % mov
      done=ecmcSlitDemoLib.moveAxisPosition(gapMotor,mov)
      if not done:
        print "%s failed to position." % gapMotor
        sys.exit()
      done=ecmcSlitDemoLib.waitForAxis(gapMotor,1800)
      if not done:
        print "%s failed waiting" % gapMotor
        sys.exit() 
      mov=76
      time.sleep(2)
    if mov == 76:
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

