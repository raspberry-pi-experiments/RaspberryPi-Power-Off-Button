"""
MIT License

Copyright (c) 2020 Marcin Sielski <marcin.sielski@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from gpiozero import Button
from subprocess import call
from signal import pause
import sys

class PowerOff:

    """
    PowerOff service executes shutdown procedure on deactivation signal raised
    on selected pin.
    """

    def __init__(self, pin):
        
        """
        Initializes PowerOff services 

        Args:
            pin (int): pin to monitor
        """
        
        self.__push_switch__ = Button(pin)
        self.__push_switch__.when_activated = self.push_switch_activated
        self.__push_switch__.when_deactivated = self.push_switch_deactivated

    
    def push_switch_activated(self):
        
        """
        Callback method executed when selected pin is activated.
        """
    
        print("Push switch activated.")

    
    def push_switch_deactivated(self):
    
        """
        Callback method executed when selected pin is deactivated.
        """
    
        print("Push switch deactivated.")
        print("Power off ...")
        call("sudo shutdown -h now", shell=True)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        poweroff = PowerOff(sys.argv[1])
        try:
            pause()
        except KeyboardInterrupt:
            pass
    else:
        print("Usage: {} pin".format(sys.argv[0]))