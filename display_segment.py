import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
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
GPIO.setwarnings(False)
def display_seg(digit):
    if digit == 0:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 1)
    elif digit == 1:
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
    elif digit == 2:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 1)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
    elif digit == 3:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
    elif digit == 4:
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        
    elif digit == 5:
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
    elif digit == 6:
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
    elif digit == 7:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
    elif digit == 8:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
    elif digit ==9:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
