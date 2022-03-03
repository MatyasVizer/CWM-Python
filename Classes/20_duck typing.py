from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

# duck typing "if it walks like a duck, and quacks like a duck; its a duck"
# doesnt check the type of objects
# only looks for existence
