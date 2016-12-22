import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class ThinkerSpacer:
    def __init__(self):
        
        # map from arduino pins to raspberry pi BCM pin numbers

        # I2C
        self.SDA = 2
        self.SCL = 3

        # Serial
        self.TX = 14
        self.RX = 15

        # Digital Input/Output
        self.D2 = 2
        self.D3 = 3
        self.D4 = 4
        self.D5 = 5
        self.D6 = 6
        self.D7 = 12
        self.D8 = 13
        self.D9 = 16
        self.D10 = 17
        self.D11 = 19
        self.D12 = 20
        self.D13 = 21
        self.D14 = 22
        self.D15 = 23
        self.D16 = 18

        # Analog Input
        self.A0 = 0
        self.A1 = 1
        self.A2 = 2
        self.A3 = 3
        self.A4 = 4
        self.A5 = 5
        self.A6 = 6
        self.A7 = 7

        # ADC
        self.CLK = 24
        self.DOUT = 25
        self.DIN = 26
        self.CS = 27
        self.SPIMOSI = self.DIN
        self.SPIMISO = self.DOUT
        self.SPICLK = self.CLK
        self.SPICS = self.CS

        # Arduino constants
        self.INPUT = GPIO.IN
        self.OUTPUT = GPIO.OUT
        self.INPUT_PULLUP = None

        # self.NOTEs
        self.NOTE_B0  = 31
        self.NOTE_C1  = 33
        self.NOTE_CS1 = 35
        self.NOTE_D1  = 37
        self.NOTE_DS1 = 39
        self.NOTE_E1  = 41
        self.NOTE_F1  = 44
        self.NOTE_FS1 = 46
        self.NOTE_G1  = 49
        self.NOTE_GS1 = 52
        self.NOTE_A1  = 55
        self.NOTE_AS1 = 58
        self.NOTE_B1  = 62
        self.NOTE_C2  = 65
        self.NOTE_CS2 = 69
        self.NOTE_D2  = 73
        self.NOTE_DS2 = 78
        self.NOTE_E2  = 82
        self.NOTE_F2  = 87
        self.NOTE_FS2 = 93
        self.NOTE_G2  = 98
        self.NOTE_GS2 = 104
        self.NOTE_A2  = 110
        self.NOTE_AS2 = 117
        self.NOTE_B2  = 123
        self.NOTE_C3  = 131
        self.NOTE_CS3 = 139
        self.NOTE_D3  = 147
        self.NOTE_DS3 = 156
        self.NOTE_E3  = 165
        self.NOTE_F3  = 175
        self.NOTE_FS3 = 185
        self.NOTE_G3  = 196
        self.NOTE_GS3 = 208
        self.NOTE_A3  = 220
        self.NOTE_AS3 = 233
        self.NOTE_B3  = 247
        self.NOTE_C4  = 262
        self.NOTE_CS4 = 277
        self.NOTE_D4  = 294
        self.NOTE_DS4 = 311
        self.NOTE_E4  = 330
        self.NOTE_F4  = 349
        self.NOTE_FS4 = 370
        self.NOTE_G4  = 392
        self.NOTE_GS4 = 415
        self.NOTE_A4  = 440
        self.NOTE_AS4 = 466
        self.NOTE_B4  = 494
        self.NOTE_C5  = 523
        self.NOTE_CS5 = 554
        self.NOTE_D5  = 587
        self.NOTE_DS5 = 622
        self.NOTE_E5  = 659
        self.NOTE_F5  = 698
        self.NOTE_FS5 = 740
        self.NOTE_G5  = 784
        self.NOTE_GS5 = 831
        self.NOTE_A5  = 880
        self.NOTE_AS5 = 932
        self.NOTE_B5  = 988
        self.NOTE_C6  = 1047
        self.NOTE_CS6 = 1109
        self.NOTE_D6  = 1175
        self.NOTE_DS6 = 1245
        self.NOTE_E6  = 1319
        self.NOTE_F6  = 1397
        self.NOTE_FS6 = 1480
        self.NOTE_G6  = 1568
        self.NOTE_GS6 = 1661
        self.NOTE_A6  = 1760
        self.NOTE_AS6 = 1865
        self.NOTE_B6  = 1976
        self.NOTE_C7  = 2093
        self.NOTE_CS7 = 2217
        self.NOTE_D7  = 2349
        self.NOTE_DS7 = 2489
        self.NOTE_E7  = 2637
        self.NOTE_F7  = 2794
        self.NOTE_FS7 = 2960
        self.NOTE_G7  = 3136
        self.NOTE_GS7 = 3322
        self.NOTE_A7  = 3520
        self.NOTE_AS7 = 3729
        self.NOTE_B7  = 3951
        self.NOTE_C8  = 4186
        self.NOTE_CS8 = 4435
        self.NOTE_D8  = 4699
        self.NOTE_DS8 = 4978

        # set up the SPI interface pins
        GPIO.setup(self.SPIMOSI, GPIO.OUT)
        GPIO.setup(self.SPIMISO, GPIO.IN)
        GPIO.setup(self.SPICLK, GPIO.OUT)
        GPIO.setup(self.SPICS, GPIO.OUT)

    def analogRead(self, adcnum):
        # read SPI data from MCP3008 chip,
        # 8 possible adc's (0 thru 7)
        
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(self.SPICS, True)
 
        GPIO.output(self.SPICLK, False)  # start clock low
        GPIO.output(self.SPICS, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(self.SPIMOSI, True)
                else:
                        GPIO.output(self.SPIMOSI, False)
                commandout <<= 1
                GPIO.output(self.SPICLK, True)
                GPIO.output(self.SPICLK, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(self.SPICLK, True)
                GPIO.output(self.SPICLK, False)
                adcout <<= 1
                if (GPIO.input(self.SPIMSIO)):
                        adcout |= 0x1
 
        GPIO.output(self.SPICS, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

    def pinMode(self, pin, mode):
        if (mode == self.INPUT_PULLUP):
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        else:
            GPIO.setup(pin, mode)

    def servo(self, pin):
        self.pinMode(pin, self.OUTPUT)
        return GPIO.PWM(pin, 50)

    def digitalWrite(self, pin, value):
        GPIO.output(pin, value)

    def digitalRead(self, pin):
        return GPIO.input(pin)

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def tone(self, pin, frequency, duration):
        self.pinMode(pin, self.OUTPUT)
        buzzer = GPIO.PWM(pin, 262)
        buzzer.start(0)
        buzzer.ChangeDutyCycle(50)
        buzzer.ChangeFrequency(frequency)
        time.sleep(duration/1000.)
        buzzer.start(0)

    def noTone(self, pin):
        self.tone(pin, 0)

    def mapRange(self, v, r1, r2):
        return (v-r1[0])/(r1[1]-r1[0]) * (r2[1]-r2[0]) + r2[0]
        
