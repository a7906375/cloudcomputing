#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:43:25 2018

@author: Abduljaber Abdulqader
"""
import argparse
import requests
import time
import httplib
import numpy as np
from numpy.random import normal
#import numpy.random.normal as normal
from numpy.random import poisson

parser = argparse.ArgumentParser()
parser.add_argument("x1", help="mu", type=float)
parser.add_argument("x2", help="sigma", type=float)
parser.add_argument("x3", help="lamda", type=float)
parser.add_argument("url", help="URL")
args = parser.parse_args()
print(args.x1)

def loadGeneratorNormal(x1,x2,url):
   nd = np.random.normal(x1, x2, 50)
   print "Normal distribution", nd
   x=len(nd)
   for i in range(x):
      print i
      res=requests.get(args.url)
      print res._content
      time.sleep(i)

def loadGeneratorPoisson(x3,url):
   #k = np.mean(x3)
   #lamda = len(number)
   pd=np.random.poisson(x3,50)
   print "Poisson distribution", pd
   x=len(pd)
   for i in range(x):
      print i
      res=requests.get(args.url)
      print res._content
      time.sleep(i)

loadGeneratorNormal(args.x1, args.x2, args.url)
loadGeneratorPoisson(args.x3, args.url)