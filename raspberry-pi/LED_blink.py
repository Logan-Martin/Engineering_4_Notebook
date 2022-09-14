import board # type: ignore
import digitalio  # type: ignore
import time

led = digitalio.DigitalInOut(board.LED) # on board LED
led.direction = digitalio.Direction.OUTPUT

redLED = digitalio.DigitalInOut(board.GP16)
redLED.direction = digitalio.Direction.OUTPUT

greenLED = digitalio.DigitalInOut(board.GP17)
greenLED.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP18) # Button frame work stuff
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

countDownNumber = 10 # this is how long the countdown should last, in seconds.
countDownMessage = "Lift off in: "

countdownHasBegun = False

while True:
    if button1.value == True and countdownHasBegun == False: # IF the button is pressed and the coundown hasn't started already, begin the countdown.
        countdownHasBegun = True
        print("Button pressed!")
        while countDownNumber > 0: 
            print(countDownMessage + str(countDownNumber)) # this combines strings to say the countdown
            redLED.value = True 
            time.sleep(0.5)
            redLED.value = False
            countDownNumber = countDownNumber - 1
            time.sleep(0.5)
        print("Lift off!")
        greenLED.value = True



