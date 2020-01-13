"""
Latch phy layer object

WARNING, ALERT, ETC

This module does not support changing the system time while running.
Don't do it
"""
from datetime import datetime, timedelta
from threading import Thread, Lock


class Latch:
    def __init__(self, gpio_object, max_on_seconds=3, hold_off_seconds=10, last_disabled=datetime.now()):
        """
        Creates a latch object with the provided parameters
        :param gpio_object: requires "on" and "off" methods
        :param max_on_seconds:
        :param hold_off_seconds:
        :param last_disabled: a datetime object for when this object was last disabled, else now.
        """
        self.__gpio = gpio_object
        self.__max_on_time = timedelta(seconds=max_on_seconds)
        self.__hold_off_time = timedelta(seconds=hold_off_seconds)
        self.__last_disabled = last_disabled
        self.__phy_lock = Lock()

    def unlatch(self):
        """
        actuate the latch
        :return:
        """
        with self.__phy_lock:
            if (datetime.now() - self.__last_disabled) < self.__hold_off_time:
                return False
            else:
                self.__gpio.on()
                return True

    def release(self):
        """
        Release the latch
        :return:
        """
        with self.__phy_lock:
            self.__gpio.off()
            self.__last_disabled = datetime.now()
