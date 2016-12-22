import ThinkerSpacer
import time, sys

class ThinkerBot:

    def __init__(self):
        self.ts = ThinkerSpacer.ThinkerSpacer()
        self.enabled = False

    def enable(self, state):
        if state:
            self.enabled = True
            self.left = self.ts.servo(self.ts.D2)
            self.right = self.ts.servo(self.ts.D4)
            self.left.start(7.5)
            self.right.start(7.5)
        else:
            self.enabled = False
            self.left.stop()
            self.right.stop()          

    def go(self, speed):
        if self.enabled:
            self.left.ChangeDutyCycle(7.5 + 2.5 * speed/100.)
            self.right.ChangeDutyCycle(7.5 - 2.5 * speed/100)

    def stop(self, speed): # speed here for the moment to stop crash (expects an argument)
        if self.enabled:
            self.left.ChangeDutyCycle(7.5)
            self.right.ChangeDutyCycle(7.5)
        
    def turn(self, speed):
        if self.enabled:
            self.left.ChangeDutyCycle(7.5 + 2.5 * speed/100.)
            self.right.ChangeDutyCycle(7.5 + 2.5 * speed/100)

    def beep(self, freq):
        if self.enabled:
            self.ts.tone(self.ts.D3, freq, 20)
            time.sleep(0.2)

    def flash(self, led):
        if self.enabled:
            pin = getattr(self.ts, "D"+str(led))
            self.ts.pinMode(pin, self.ts.OUTPUT)
            self.ts.digitalWrite(pin, 1)
            time.sleep(0.2)
            self.ts.digitalWrite(pin, 0)
            time.sleep(0.2)
                                 
                 
