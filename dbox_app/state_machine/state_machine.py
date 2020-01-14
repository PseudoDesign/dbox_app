from transitions import Machine
from dbox_app.rgb_led import Color
from transitions.extensions.states import add_state_features, Timeout


@add_state_features(Timeout)
class TimeoutStateMachine(Machine):
    pass


class StateMachine(object):

    states = [
        'entry',
        'idle',
        {
            'name': 'unlatch_failure',
            'timeout': 3,
            'on_timeout': 'advance',
            'ignore_invalid_triggers': True,
            'on_enter': 'enter_unlatch_failure_state',
            'on_exit': 'exit_unlatch_failure_state',
        },
        {
            'name': 'unlatch',
            'timeout': 3,
            'on_timeout': 'advance',
            'ignore_invalid_triggers': True,
            'on_enter': 'enter_unlatch_state',
            'on_exit': 'exit_unlatch_state'
        },
    ]

    def __init__(self, button, led, secure_lock, bluetooth, latch):
        """
        Main state machine for the application.  Implements the "transitions" library
        :param button:
        :param led:
        :param secure_lock:
        :param bluetooth:
        :param latch:
        """
        self.__button = button
        self.__led = led
        self.__secure_lock = secure_lock
        self.__bluetooth = bluetooth
        self.__latch = latch

        self.machine = TimeoutStateMachine(model=self, states=self.states, initial='entry')

        # Set up button press handler
        self.machine.add_transition(
            "trigger_button_press",
            "idle",
            "unlatch_failure",
            conditions=['is_device_locked'],
        )
        self.machine.add_transition(
            "trigger_button_press",
            "idle",
            "unlatch"
        )
        self.__button.on_press_and_release = self.trigger_button_press
        # Transitions back to idle
        self.machine.add_transition(
            "advance",
            "unlatch_failure",
            "idle",
        )
        self.machine.add_transition(
            "advance",
            "unlatch",
            "idle",
        )

    def is_device_locked(self):
        """
        Returns true if the device is locked, else false
        :return:
        """
        return self.__secure_lock.is_locked

    def enter_unlatch_failure_state(self):
        """
        Tasks to run when entering the unlatch failure state
        :return:
        """
        self.__led.disable()
        self.__led.set_color(Color.RED)
        self.__led.set_fade(False)
        self.__led.set_blink_frequency(4)
        self.__led.enable()

    def exit_unlatch_failure_state(self):
        """
        Tasks to run when exiting the unlatch failure state
        :return:
        """
        self.__led.disable()

    def enter_unlatch_state(self):
        self.__led.disable()
        if self.__latch.actuate():
            self.__led.set_color(Color.GREEN)
        else:
            self.__led.set_color(Color.PINK)
        self.__led.set_fade(True)
        self.__led.set_blink_frequency(2)
        self.__led.enable()

    def exit_unlatch_state(self):
        self.__latch.release()
        self.__led.disable()


