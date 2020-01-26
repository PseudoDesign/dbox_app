from .state_machine import StateMachine
from .lock_authorization import SecureLock
from .phy import Button, Latch, RgbLed
import argparse
import yaml
import signal
import sdnotify
from time import sleep


class SignalHandler:
    exit = True

    def __init__(self):
        signal.signal(signal.SIGINT, self.set_exit_flag)
        signal.signal(signal.SIGTERM, self.set_exit_flag)

    @classmethod
    def set_exit_flag(cls):
        """
        set the exit flag to TRUE
        :return:
        """
        cls.exit = True


def main():
    sd_notify = sdnotify.SystemdNotifier()
    signal_handler = SignalHandler()
    parser = argparse.ArgumentParser(description="Launcher for the dbox app")
    parser.add_argument('-c', '--config_file', type=str, default="/etc/dbox/conf", help="Location of the config file")

    args = parser.parse_args()

    # Open the yaml file and ensure parameters are in the file
    try:
        with open(args.config_file, 'r') as fpt:
            config_data = yaml.safe_load(fpt)
            button_pin = int(config_data["button"])
            latch_pin = int(config_data["latch"])
            red_led_pin = int(config_data["led_r"])
            green_led_pin = int(config_data["led_g"])
            blue_led_pin = int(config_data["led_b"])
            secure_lock_file = config_data["lock_file"]
    except FileNotFoundError:
        raise FileNotFoundError(f"Unable to open config file {args.config_file}.  See README for details")
    except (KeyError, yaml.YAMLError):
        raise ValueError(f"Invalid config file {args.config_file}.  See README for details")

    button = Button(button_pin)
    latch = Latch(latch_pin)
    led = RgbLed(red_led_pin, green_led_pin, blue_led_pin)
    lock = SecureLock(secure_lock_file)

    machine = StateMachine(button, led, lock, None, latch)

    machine.start()
    sd_notify.notify("READY=1")

    while not signal_handler.exit:
        sd_notify.notify("WATCHDOG=1")
        sleep(1)

    sd_notify.notify("STOPPING=1")

    button.close()
    latch.close()
    led.close()
