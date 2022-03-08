from gpiozero import LED, Button
from signal import pause

led = LED(4)
button = Button(5)
button2 = Button(6)
button.when_pressed = led.on
button2.when_pressed = led.off
pause()
