# Title: Cat.py
# Path: IP4RIOT-Classwork\sessions\session_15\Cat.py
#
# Desc: Example class to demonstrate unit testing
# Author: Reina Rowlands (20066312)
# Date: 2025-05-30
#

class Cat:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat

    def speak(self):
        return f"{self.name} with {self.coat} Meows."
