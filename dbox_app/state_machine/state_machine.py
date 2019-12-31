from transitions import Machine
from dbox_app.rgb_led import Color
from transitions.extensions.states import add_state_features, Timeout


@add_state_features(Timeout)
class CustomStateMachine(Machine):
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
        },
    ]

    def __init__(self, button, led, secure_lock, bluetooth):
        self.__button = button
        self.__led = led
        self.__secure_lock = secure_lock
        self.__bluetooth = bluetooth

        self.machine = CustomStateMachine(model=self, states=self.states, initial='entry')

        self.machine.add_transition(
            "trigger_button_press",
            "idle",
            "unlatch_failure",
        )

        self.machine.on_enter_unlatch_failure('enter_unlatch_failure_state')
        self.machine.on_exit_unlatch_failure('exit_unlatch_failure_state')

        self.__button.on_press_and_release = self.trigger_button_press

        self.machine.add_transition(
            "advance",
            "unlatch_failure",
            "idle",
        )

    def enter_unlatch_failure_state(self):
        self.__led.set_color(Color.RED)
        self.__led.set_fade(False)
        self.__led.set_blink_frequency(2)
        self.__led.enable()

    def exit_unlatch_failure_state(self):
        self.__led.disable()


