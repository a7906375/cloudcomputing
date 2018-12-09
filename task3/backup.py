#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:43:25 2018

@author: student
"""
import numpy as np
from numpy.random import normal
#import numpy.random.normal as normal
from numpy.random import poisson
#import urllib2

#url = urllib2.urlopen("http://localhots:8080").read()

def loadGeneratorNormal(x1,x2):
   n=["10"]
   mu = np.mean(x1)
   sigma = np.std(x2)
   nd = np.random.normal(mu, sigma, 10)
   #nd = np.random.normal(mu, sigma, len(n))
   #return d
   print "Normal distribution", nd
     
      
def loadGeneratorPoisson(x3):
   number=[10]
   k = np.mean(x3)
   #lamda = len(number)
   pd = poisson (k, 10)
   #return d
   print "Poisson distribution", pd

loadGeneratorNormal(0.1,50)
loadGeneratorPoisson(15)
    