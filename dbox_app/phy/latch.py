"""
Latch phy layer object

WARNING, ALERT, ETC

This module does not support changing the system time while running.
Don't do it
"""
from datetime import datetime, timedelta
from threading import Thread, Lock
from time import sleep
from gpiozero import DigitalOutputDevice


class Latch:
    def __init__(self,
                 pin: int,
                 max_on_seconds: float = 3,
                 hold_off_seconds: float = 10,
                 last_disabled: datetime = datetime.now()):
        """
        Creates a latch object with the provided parameters
        :param pin: pin number
        :param max_on_seconds:
        :param hold_off_seconds:
        :param last_disabled: a datetime object for when this object was last disabled, else now.
        """
        self.__gpio = DigitalOutputDevice(pin)
        self.__max_on_time = timedelta(seconds=max_on_seconds)
        self.__hold_off_time = timedelta(seconds=hold_off_seconds)
        self.__last_disabled = last_disabled
        self.__phy_lock = Lock()
        self.__background_thread = None
        self.__stop_thread = False

    def _unlatch_after_max_hold_time(self):
        start_time = datetime.now()
        while 1:
            if (datetime.now() - start_time) >= self.__max_on_time:
                with self.__phy_lock:
                    self.__gpio.off()
                break
            with self.__phy_lock:
                if self.__stop_thread:
                    break
            sleep(.1)

    def unlatch(self):
        """
        actuate the latch
        :return:
        """
        with self.__phy_lock:
            if (datetime.now() - self.__last_disabled) < self.__hold_off_time:
                return False
            else:
                if self.__background_thread is None:
                    self.__background_thread = Thread(target=self._unlatch_after_max_hold_time)
                    self.__stop_thread = False
                    self.__background_thread.start()
                self.__gpio.on()
                return True

    def release(self):
        """
        Release the latch and stop the background thread
        :return:
        """
        with self.__phy_lock:
            self.__gpio.off()
            self.__last_disabled = datetime.now()
            if self.__background_thread is not None:
                self.__stop_thread = True
        if self.__background_thread is not None:
            self.__background_thread.join()
            self.__stop_thread = False

    def close(self):
        with self.__phy_lock:
            self.__gpio.off()
            self.__last_disabled = datetime.now()
            if self.__background_thread is not None:
                self.__stop_thread = True
        if self.__background_thread is not None:
            self.__background_thread.join()
        self.__gpio.close()
