from typing import Union
from gpiozero import Button as PhyButton


class Button(PhyButton):
    def __init__(self, pin: Union[int, str], hold_time=3, active_high=True, pull_up=None, **kwargs):
        """
        Extend the gpiozero Button class to include press-and-release functionality
        :param pin: GPIO number
        """
        super().__init__(pin, hold_time=hold_time, active_state=active_high, pull_up=pull_up, **kwargs)
        self.__was_held = False
        self.on_press_and_release = None
        self.on_hold = None
        self.when_pressed = self._on_phy_press
        self.when_released = self._on_phy_release
        self.when_held = self._on_phy_hold

    def _on_phy_press(self):
        self.__was_held = False

    def _on_phy_release(self):
        if not self.__was_held:
            if self.on_press_and_release is not None:
                self.on_press_and_release()

    def _on_phy_hold(self):
        self.__was_held = True
        if self.on_press_and_release is not None:
            self.on_hold()
