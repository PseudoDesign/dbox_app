import gpiozero
from .color import Color


class RgbLed:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.__led = gpiozero.RGBLED(red_pin, green_pin, blue_pin)
        self.__color = Color.WHITE

    def set_color(self, color):
        self.__color = color
        self.__led.color = color

    def disable(self):
        self.__led.off()

    def blink(self, frequency, fade=False):
        on_time = frequency/2.0
        if fade:
            self.__led.pulse(fade_in_time=on_time, fade_out_time=on_time, on_color=self.__color)
        else:
            self.__led.blink(on_time=on_time, off_time=on_time, on_color=self.__color)

    def close(self):
        self.__led.close()