from transitions.extensions import LockedMachine as Machine
from dbox_app.phy.rgb_led import Color
from transitions.extensions.states import add_state_features, Timeout


@add_state_features(Timeout)
class TimeoutStateMachine(Machine):
    pass


class StateMachine(object):

    states = [
        {
            'name': 'startup',
            'ignore_invalid_triggers': True,
        },
        {
            'name': 'idle',
            'ignore_invalid_triggers': True,
        },
        {
            'name': 'unlatch_failure',
            'timeout': 3,
            'on_timeout': 'advance',
            'ignore_invalid_triggers': True,
            'on_enter': '_enter_unlatch_failure_state',
            'on_exit': '_exit_unlatch_failure_state',
        },
        {
            'name': 'unlatch',
            'timeout': 3,
            'on_timeout': 'advance',
            'ignore_invalid_triggers': True,
            'on_enter': '_enter_unlatch_state',
            'on_exit': '_exit_unlatch_state'
        },
        {
            'name': 'exiting',
            'ignore_invalid_triggers': True,
        }
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

        self.machine = TimeoutStateMachine(model=self, states=self.states, initial='idle')

        # Set up the startup state transition
        self.machine.add_transition(
            "_on_start",
            "startup",
            "idle",
        )

        # Set up button press handler
        self.machine.add_transition(
            "_trigger_button_press",
            "idle",
            "unlatch_failure",
            conditions=['_is_device_locked'],
        )
        self.machine.add_transition(
            "_trigger_button_press",
            "idle",
            "unlatch"
        )
        self.__button.on_press_and_release = self._trigger_button_press

        # Transitions back to idle from button press handlers
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

        # Set up the exit transitions
        self.machine.add_transition(
            "_on_exit",
            "idle",
            "exiting"
        )
        self.machine.add_transition(
            "_on_exit",
            "unlatch_failure",
            "exiting"
        )
        self.machine.add_transition(
            "_on_exit",
            "unlatch",
            "exiting"
        )

    def start(self):
        """
        Move the state machine from the startup to idle state
        :return:
        """
        self._on_start()

    def exit(self):
        """
        Begin the state machine exit procedure
        :return:
        """
        self._on_exit()

    def _is_device_locked(self):
        """
        Returns true if the device is locked, else false
        :return:
        """
        return self.__secure_lock.is_locked


    def _enter_unlatch_failure_state(self):
        """
        Tasks to run when entering the unlatch failure state
        :return:
        """
        self.__led.disable()
        self.__led.set_color(Color.RED)
        self.__led.blink(4)
        self.__led.enable()

    def _exit_unlatch_failure_state(self):
        """
        Tasks to run when exiting the unlatch failure state
        :return:
        """
        self.__led.disable()

    def _enter_unlatch_state(self):
        self.__led.disable()
        if self.__latch.actuate():
            self.__led.set_color(Color.GREEN)
        else:
            self.__led.set_color(Color.PINK)
        self.__led.blink(2, fade=True)

    def _exit_unlatch_state(self):
        self.__latch.release()
        self.__led.disable()


