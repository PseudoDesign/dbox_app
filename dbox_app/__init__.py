from .state_machine import StateMachine
from .lock_authorization import SecureLock
from .phy import Button, Latch, RgbLed
import argparse
import yaml


def main():
    parser = argparse.ArgumentParser(description="Launcher for the dbox app")
    parser.add_argument('config_file', type=str, default="/etc/dbox/conf", help="Location of the donfi")

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