import board # type: ignore
import digitalio  # type: ignore
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

countDownNumber = 10
countDownMessage = "Lift off in: "

while countDownNumber > 1:
    print(countDownMessage + str(countDownNumber))
    time.sleep(1)
    countDownNumber = countDownNumber - 1
print("Lift off!")
