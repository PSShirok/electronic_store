from src.keyboard import Keyboard

keyb = Keyboard('Keron', 3200, 1)
assert keyb.language == "EN"
keyb.change_lang()
assert keyb.language == "RU"