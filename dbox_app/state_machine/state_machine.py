from transitions import Machine


class StateMachine(object):

    states = ['entry', 'idle', 'unlatch_failure']

    def __init__(self, button, led, secure_lock, bluetooth):
        self.__button = button
        self.__led = led
        self.__secure_lock = secure_lock
        self.__bluetooth = bluetooth

        self.machine = Machine(model=self, states=self.states, initial='entry')

        self.machine.add_transition(
            "button_press_and_release",
            "idle",
            "unlatch_failure",
        )

        self.__button.on_press_and_release = self.on_button_press_and_release

    def on_button_press_and_release(self):
        self.button_press_and_release()
