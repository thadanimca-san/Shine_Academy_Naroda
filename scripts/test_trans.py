from googletrans import Translator
import time

def test():
    translator = Translator()
    text = "Hello, how are you?"
    hi = translator.translate(text, dest='hi').text
    gu = translator.translate(text, dest='gu').text
    print(f"HI: {hi}")
    print(f"GU: {gu}")

test()
