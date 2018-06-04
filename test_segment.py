#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import display_segment
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 23
B = 19
C = 15
D = 11
E = 13
F = 5
G =3
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
l = 0
while l <= 9:
    display_segment.display_seg(l)
    l = l+1
    time.sleep(1)
    if l > 9:
        break
        
GPIO.cleanup()

