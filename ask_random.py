#!/usr/bin/env python
import os, sys, random

def main():
    print "YC Interview Practice - by @shauvik"
    print "==================================="

    questions = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            for line in open(file):
                if(not line.startswith('Section')):
                    questions.append(line)

    print "You will be asked questions one by one."
    print "Adjust font-size using Ctrl+/-"
    print "Press any key to proceed through questions... (Ctrl X to quit)"
    wait_key()
    while(True):
        line = random.choice(questions)
        os.system('clear')
        os.system('echo '+line)
        os.system('say -r 400 '+line)
        wait_key()

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    return result

if __name__ == '__main__':
    main()