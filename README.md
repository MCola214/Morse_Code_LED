# Morse_Code_LED

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
A simple beginner Raspberry Pi project using an RPi 4, RPi.GPIO, and an LED. Using the terminal, the RPi will take user text input and flash the translated morse code sequence using the attached LED.

To properly see the visual output from the LED, connect an LED of your choice to pin 11 (GPIO17).
	
## Technologies
Project is created with:
* Python: 3.7.3
* RPi.GPIO: 0.7.0
	
## Setup
To run this project, ensure you have the RPi.GPIO package installed and use python 3:

```
$ pip install RPi.GPIO
$ python3 MorseCode.py
```
Or, if you have python 3 as the default on your machine:
```
$ python MorseCode.py
```