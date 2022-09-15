# Engineering_4_Notebook

&nbsp;
## Table of Contents
* [Raspberry_Pi_Assignment_Template](#Raspberry_Pi_Assignment_Template)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)


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



## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
 [Link to raspberry-pi temp](raspberry-pi)
### Test Image
![Spicy Sticker](images/spicyStickerImage.jpg)  
### Test GIF
![Bread Fall Gif](images/falling-bread-bread.gif)  
