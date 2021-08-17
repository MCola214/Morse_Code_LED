import RPi.GPIO as GPIO
import time
from enum import Enum

# set the GPIO pin to be used for the LED as 11 (GPIO17)
ledPin = 11

# configure the GPIO settings
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('Using pin%d'%ledPin)

# on program end, properly close GPIO
def destroy():
    print("\n")
    GPIO.cleanup()

class Blink(Enum):
    DOT = 1
    DASH = 2
    SPACE = 3

# return the blink sequence for the given character, or an empty array if given an uncoded char
def getLetterSequence(letter):
    codeSeq = {
        'A': [Blink.DOT, Blink.DASH], 
        'B': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT],
        'C': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT], 
        'D': [Blink.DASH, Blink.DOT, Blink.DOT], 
        'E': [Blink.DOT], 
        'F': [Blink.DOT, Blink.DOT, Blink.DASH, Blink.DOT], 
        'G': [Blink.DASH, Blink.DASH, Blink.DOT], 
        'H': [Blink.DOT, Blink.DOT, Blink.DOT,  Blink.DOT], 
        'I': [Blink.DOT, Blink.DOT], 
        'J': [Blink.DOT, Blink.DASH, Blink.DASH, Blink.DASH], 
        'K': [Blink.DASH, Blink.DOT, Blink.DASH], 
        'L': [Blink.DOT, Blink.DASH, Blink.DOT, Blink.DOT], 
        'M': [Blink.DASH, Blink.DASH], 
        'N': [Blink.DASH, Blink.DOT], 
        'O': [Blink.DASH, Blink.DASH, Blink.DASH], 
        'P': [Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT], 
        'Q': [Blink.DASH, Blink.DASH, Blink.DOT, Blink.DASH], 
        'R': [Blink.DOT, Blink.DASH, Blink.DOT], 
        'S': [Blink.DOT, Blink.DOT, Blink.DOT], 
        'T': [Blink.DASH], 
        'U': [Blink.DOT, Blink.DOT, Blink.DASH], 
        'V': [Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH], 
        'W': [Blink.DOT, Blink.DASH, Blink.DASH], 
        'X': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DASH], 
        'Y': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DASH], 
        'Z': [Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT], 
        '0': [Blink.DASH, Blink.DASH, Blink.DASH, Blink.DASH, Blink.DASH],
        '1': [Blink.DOT, Blink.DASH, Blink.DASH, Blink.DASH, Blink.DASH],
        '2': [Blink.DOT, Blink.DOT, Blink.DASH, Blink.DASH, Blink.DASH, ],
        '3': [Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH, Blink.DASH],
        '4': [Blink.DOT, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH],
        '5': [Blink.DOT, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DOT],
        '6': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DOT],
        '7': [Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT],
        '8': [Blink.DASH, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT],
        '9': [Blink.DASH, Blink.DASH, Blink.DASH, Blink.DASH, Blink.DOT],
        '.': [Blink.DOT, Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT, Blink.DASH],
        ',': [Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DASH, Blink.DASH],
        '?': [Blink.DOT, Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT],
        "'": [Blink.DOT, Blink.DASH, Blink.DASH, Blink.DASH, Blink.DASH, Blink.DOT],
        '!': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT, Blink.DASH, Blink.DASH],
        '/': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DASH, Blink.DOT],
        '(': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT],
        ')': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DASH],
        '&': [Blink.DOT, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT],
        ':': [Blink.DASH, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT],
        ';': [Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT],
        '=': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH],
        '+': [Blink.DOT, Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT],
        '-': [Blink.DASH, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH],
        '_': [Blink.DOT, Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DASH],
        '"': [Blink.DOT, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DASH, Blink.DOT],
        '$': [Blink.DOT, Blink.DOT, Blink.DOT, Blink.DASH, Blink.DOT, Blink.DOT, Blink.DASH],
        '@': [Blink.DOT, Blink.DASH, Blink.DASH, Blink.DOT, Blink.DASH, Blink.DOT],
        ' ': [Blink.SPACE]
    }

    return codeSeq.get(letter.upper(), [])

# set GPIO pin to HIGH or LOW with appropriate timing
def flashLED(blinkType):

    # create switch statement using dict and function values
    def case_dot():
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.3)

    def case_dash():
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.3)

    def case_space():
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(2)

    def default():
        print("Unknown input: " + blinkType)

    switcher = {
            Blink.DOT: case_dot,
            Blink.DASH: case_dash,
            Blink.SPACE: case_space
    }

    switcher.get(blinkType, default)()

def endLetter():
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.5)

# main loop to get user input and translate to morse code
def loop():
    while True:
        sentence = input("Enter sentence to convert to morse code\n")
        for letter in sentence:
            print("Sequence for: " + letter)
            letterSeq = getLetterSequence(letter)
            for blink in letterSeq:
                flashLED(blink)
            endLetter()


if __name__ == '__main__':
    print('Starting morse code LED...\n')
    setup()
    try:
        loop()
        destroy()
    except KeyboardInterrupt:
        destroy()
