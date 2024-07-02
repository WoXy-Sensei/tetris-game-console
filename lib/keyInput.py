import digitalio
import board


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class KeyInput:
    def __init__(self, A=board.GP9, B=board.GP13, X=board.GP14, Y=board.GP15):
        self.A = A
        self.B = B
        self.X = X
        self.Y = Y

        self.btn1 = digitalio.DigitalInOut(self.A)
        self.btn1.switch_to_input(pull=digitalio.Pull.UP)

        self.btn2 = digitalio.DigitalInOut(self.B)
        self.btn2.switch_to_input(pull=digitalio.Pull.UP)

        self.btn3 = digitalio.DigitalInOut(self.Y)
        self.btn3.switch_to_input(pull=digitalio.Pull.UP)

        self.btn4 = digitalio.DigitalInOut(self.X)
        self.btn4.switch_to_input(pull=digitalio.Pull.UP)

        self.buttons = {
            "A": self.btn1,
            "B": self.btn2,
            "X": self.btn3,
            "Y": self.btn4
        }

        self.buttons_status = {
            "A": False,
            "B": False,
            "X": False,
            "Y": False
        }

    def isHoldKey(self, button):
        self.buttons_status[button] = not (self.buttons[button].value)
        return self.buttons_status[button]

    def isPressedKey(self, button):
        if (self.buttons_status[button] == False and not (self.buttons[button].value) == True):
            self.buttons_status[button] = not (self.buttons[button].value)
            return True

        self.buttons_status[button] = not (self.buttons[button].value)
        return False

    def isReleaseKey(self, button):
        if (self.buttons_status[button] == True and not (self.buttons[button].value) == False):
            return True
        self.buttons_status[button] = not (self.buttons[button].value)
        return False
