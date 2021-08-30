from pyfirmata import Arduino, SERVO
port = 'COM5'
pin = 10
board = Arduino(port)
board.digital[pin].mode = SERVO
def rotate(pin,angle):
    board.digital[pin].write(angle)
def autodoor(val):
    if val==0:
        rotate(pin,120)
    elif val==1:
        rotate(pin,0)
