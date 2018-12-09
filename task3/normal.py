#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:43:25 2018

@author: student
"""
import argparse
import requests
import time
import httplib
import numpy as np
from numpy.random import normal
#import numpy.random.normal as normal
from numpy.random import poisson
#import urllib2
#url = 'http://localhost:8080/primecheck'

parser = argparse.ArgumentParser()
parser.add_argument("x1", help="mu", type=float)
parser.add_argument("x2", help="sigma", type=float)
#parser.add_argument("x3", help="lamda")
#parser.add_argument("x4", help="concurrent time")
parser.add_argument("url", help="URL")
args = parser.parse_args()
print(args.x1)

def loadGeneratorNormal(x1,x2,url):
   # n=["10"]
   # mu = np.mean(x1)
   # sigma = np.std(x2)
   #nd = np.random.normal(x1, x2, x4)
   #nd = np.random.normal( x1,x2,50)
   #nd = np.random.normal(float(x1), float(x2), 50)
   nd = np.random.normal(x1, x2, 50)
   print "ddd", nd
   x=len(nd)
   for i in range(x):
      print i
      res=requests.get(args.url)
      #print time ms
      print res._content
      #res = requests.get("http://localhost:8080/primecheck")
      time.sleep(i)
   #nd = np.random.normal(mu, sigma, len(n))
   #return nd
   print "Normal distribution", nd


loadGeneratorNormal(args.x1, args.x2, args.url)

#def loadGeneratorPoisson(x3):
   #number=[10]
   #k = np.mean(x3)
   #lamda = len(number)
   #pd = poisson (k, 10)
   #return pd
   #print "Poisson distribution", pd

#loadGeneratorPoisson(15)
#while True: 
     
  #res=requests.get(args.url)
  #res.text
  #print "res", res.text
  #time.sleep(5)
