import requests
import argparse
import time
import httplib
import numpy as np
from numpy.random import poisson

parser = argparse.ArgumentParser()
parser.add_argument("x3", type=float, help="lamda")
parser.add_argument("url", help="URL")
args = parser.parse_args()
print(args.x3)

def loadGeneratorPoisson(x3,url):
   #k = np.mean(x3)
   #lamda = len(number)
   pd=np.random.poisson(x3,5)
   x=len(pd)
   for i in range(x):
      print i
      res=requests.get(args.url)
      print res._content
      time.sleep(i)
   print "Poisson distribution", pd

loadGeneratorPoisson(args.x3, args.url)
