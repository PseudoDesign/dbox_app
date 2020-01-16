from .state_machine import StateMachine
from .lock_authorization import SecureLock
from .phy import Button, Latch, RgbLed


def main():
    button = Button(3)
    latch = Latch(2)
    led = RgbLed(17, 4, 18)
    lock = SecureLock("/nvm/test_lock.yaml")

    machine = StateMachine(button, led, lock, None, latch)
