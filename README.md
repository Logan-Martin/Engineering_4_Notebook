# Engineering_4_Notebook

&nbsp;
## Table of Contents
* [Launch Pad Part 1](#Launch_Pad_Part_1_(Countdown))
* [Launch Pad Part 2](#Launch_Pad_Part_2_(Lights))
* [Launch Pad Part 3](#Launch_Pad_Part_3_(Button))
* [Launch Pad Part 4](#Launch_Pad_Part_4_(Servo))



&nbsp;
## Launch Pad Part 1 (Countdown)
#### Assignment: Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.

https://user-images.githubusercontent.com/71342159/190177536-60bced6a-d8a5-4760-97a8-236c39c09282.mp4

<img src="https://user-images.githubusercontent.com/71342159/190178442-9cae21a9-acf5-4c73-b093-4f1111e26082.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchpadCodeFolder/Launchpad1Code)

#### Reflection:
I felt like I had no idea what I was doing and tried doing everything on the first launch pad assignment. Wiring was kind of an issue, but google exists along with the stuff provided in the assignment so everything was fine. To throw a lesson out there, check out strings and concatenating things. "Countdown: 10" is nicer than "10". 
&nbsp;


&nbsp;
## Launch Pad Part 2 (Lights)
#### Assignment: Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.

https://user-images.githubusercontent.com/71342159/190190369-0d09ca60-f6df-4a7c-9193-2970ff83d496.mp4

<img src="https://user-images.githubusercontent.com/71342159/190178442-9cae21a9-acf5-4c73-b093-4f1111e26082.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchpadCodeFolder/Launchpad2Code)

#### Reflection:
Not much to reflect on. Make sure you have a resistor for your LED, remember the long end is positive, use OUTPUT, turn value to true/false.
&nbsp;


&nbsp;
## Launch Pad Part 3 (Button)
#### Assignment: Include a physical button that starts the countdown. 

https://user-images.githubusercontent.com/71342159/190427455-b35110a5-d97b-4436-bd9d-c97473b464cf.mp4

<img src="https://user-images.githubusercontent.com/71342159/190178442-9cae21a9-acf5-4c73-b093-4f1111e26082.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchpadCodeFolder/Launchpad3Code)

#### Reflection:
Forgot what lines of code I needed for this to work. A couple minutes later button prints stuff and yeah. There are two ways of connecting a button apparently, do the one that makes the button print "True" because that makes more sense. Use INPUT, not OUTPUT. Make sure you pull up/down resistors, I don't really understand it but it makes it work: 
```
button1 = digitalio.DigitalInOut(board.GP18)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN
```
&nbsp;


&nbsp;
## Launch Pad Part 4 (Servo)
#### Assignment: Actuate a 180 degree servo on liftoff to simulate the launch tower disconnecting.

https://user-images.githubusercontent.com/71342159/190658767-93088c80-a5eb-4f8d-89ba-7f146ba9d465.mp4

<img src="https://user-images.githubusercontent.com/71342159/190659024-2af2c910-b1e3-4ac4-9c8a-8e744739f728.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchpadCodeFolder/Launchpad4Code)

#### Reflection:
Make sure you have everything wired up correctly with the servo, pretty easy to follow as there were instructions. Oh, I guess also make sure you grab the correct servo.
&nbsp;


&nbsp;
## Crash Avoidance Part 1 (Accelerometer)
#### Assignment: The module must have an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor.

https://user-images.githubusercontent.com/71342159/191042721-9f2a09b5-b735-4e9e-8864-6b65203d9a9d.mp4

<img src="https://user-images.githubusercontent.com/71342159/191043382-f2dac862-3abe-4dce-ae4c-f1a0b51c2f36.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance%20Part%201%20Code)

#### Reflection:
Pretty easy to follow, the printing thing was new, using fstring. I added the strings together to make sense of the info given in the prints. Gyro & Acceleration. 
&nbsp;


&nbsp;
## Crash Avoidance Part 2 (Light + Powerboost)
#### Assignment:
1. The module must have an accelerometer that continuously reports x, y, and z acceleration values.
2. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. 
3. The module must be powered by a mobile power source. 

https://user-images.githubusercontent.com/71342159/191521487-4403ba4e-216d-41b9-87df-05f9b2d2ea82.mp4

<img src="https://user-images.githubusercontent.com/71342159/191522539-00bb30d9-dbcf-44cd-ae14-5ce34372ff9b.jpg"  width="300" height="400" />

[Link to Code.](https://github.com/Logan-Martin/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance%20Assignments/Crash%20Avoidance%20Part%202%20Code)

#### Reflection:
Make sure you do CTRL+S to save code, make sure the battery is charged, and that your wiring is all good. I'd say the hardest thing about this for me was just dealing with VS code, well, it was really my fault not VS code' but yeah.
&nbsp;

### Test Link
 [Link to raspberry-pi temp](raspberry-pi)
### Test Image
![Spicy Sticker](images/spicyStickerImage.jpg)  
### Test GIF
![Bread Fall Gif](images/falling-bread-bread.gif)  
