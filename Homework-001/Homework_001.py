'''
Author : F323RED
Date : 2020/9/26
Version : 0.1.0
Describe : Python homework-001
'''

#import matplotlib
import pylab as lab
import math

def F(x) :      # Define function F()
    return max(abs(x * math.sin(x)), abs(x * math.cos(x)))

def G(x) :      # Define function G()
    return min(abs(x * math.sin(x)), abs(x * math.cos(x)))

#---------------------
# Begining of program

a = 2 * math.pi
b = -a                          # X c [-2 * PI, 2 * PI]
n = 1000                        # Number of points
deltaX = (a - b) / (n - 1)      # Delta of each points

listX = [b + i * deltaX for i in range(n)]
listY1 = [F(i) for i in listX ]
listY2 = [G(i) for i in listX ]

lab.plot(listX, listY1)         # Draw graph of F(x)
lab.plot(listX, listY2)         # Draw graph of G(x)

lab.show()                      # Show graph