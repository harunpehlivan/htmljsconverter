import sys
import time

def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

printy('Welcome to Html to JS converter.')

print('')

printy('Please type the Html code that you')
printy('want to convert into JS code.')

print('')
JS = input()

printy('The JS code for that, is')
printy('document.write("'+ JS+'");')