import board # type: ignore
import digitalio  # type: ignore
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

redLED = digitalio.DigitalInOut(board.GP16)
redLED.direction = digitalio.Direction.OUTPUT

countDownNumber = 10
countDownMessage = "Lift off in: "

while countDownNumber > 0:
    print(countDownMessage + str(countDownNumber))
    redLED.value = True
    time.sleep(0.5)
    redLED.value = False
    countDownNumber = countDownNumber - 1
    time.sleep(0.5)
print("Lift off!")
led.value = True
