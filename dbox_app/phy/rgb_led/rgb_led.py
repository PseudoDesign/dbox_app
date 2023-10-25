from typing import Union
import gpiozero
from .color import Color


class RgbLed:
    """
    This class controls a 3-color RGB LED using the gpiozero library.  It is intended for use on a Raspberry Pi
    """
    def __init__(self, red_pin: Union[int, str], green_pin: Union[int, str], blue_pin: Union[int, str]):
        """
        Create an instance of an RGB LED.  Pin parameters must be integers conforming to the Rpi GPIO spec
        See the readme for details.
        :param red_pin: The GPIO used for the Red LED
        :param green_pin: The GPIO used for the Green LED
        :param blue_pin: The GPIO used for the Blue LED
        """
        self.__led = gpiozero.RGBLED(red_pin, green_pin, blue_pin)
        self.__color = Color.WHITE

    def set_color(self, color: Color):
        """
        Set the LED color used when blinking
        :param color:
        :return:
        """
        self.__color = color
        self.__led.color = color

    def disable(self):
        """
        Turn off the LED
        :return:
        """
        self.__led.off()

    def blink(self, frequency: float, fade: bool = False):
        """
        Set the LED to blink at the provided frequency.
        :param frequency: Blinking frequency, with a 50% duty cycle
        :param fade: Enable fading the LED in and out rather than a solid blink
        :return:
        """
        on_time = frequency/2.0
        if fade:
            self.__led.pulse(fade_in_time=on_time, fade_out_time=on_time, on_color=self.__color)
        else:
            self.__led.blink(on_time=on_time, off_time=on_time, on_color=self.__color)

    def close(self):
        """
        Safely close this LED object
        :return:
        """
        self.__led.close()
