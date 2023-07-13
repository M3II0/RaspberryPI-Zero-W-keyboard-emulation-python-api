#!/usr/bin/env python3

import time

# Settings

lang = "en"

#
# Values
#

NULL_CHAR = chr(0)
RELEASE_KEY = NULL_CHAR*8

staticKeys = {
    'enter': chr(40),
    'backspace': chr(42),
    'tab': chr(4),
    'space': chr(44)
}

shortcutsShortcut = {
    'shift': chr(2),
    'ctrl': chr(1),
    'alt': chr(4),
    'win': chr(8),
    'shift-ctrl': chr(3),
    'shift-alt': chr(6),
    'shift-ctrl-alt': chr(7),
    'ctrl-win': chr(9),
    'shift-win': chr(10),
    'shift-ctrl-win': chr(11),
    'alt-win': chr(12),
    'ctrl-alt-win': chr(13),
    'shift-alt-win': chr(14),
    'shift-ctrl-alt-win': chr(15),
    'ctrl-alt': chr(5)
}

legacySymbols = {
    ' ': chr(44),
    'a': chr(4),
    'b': chr(5),
    'c': chr(6),
    'd': chr(7),
    'e': chr(8),
    'f': chr(9),
    'g': chr(10),
    'h': chr(11),
    'i': chr(12),
    'j': chr(13),
    'k': chr(14),
    'l': chr(15),
    'm': chr(16),
    'n': chr(17),
    'o': chr(18),
    'p': chr(19),
    'q': chr(20),
    'r': chr(21),
    's': chr(22),
    't': chr(23),
    'u': chr(24),
    'v': chr(25),
    'w': chr(26),
    'x': chr(27),
    'y': chr(29),
    'z': chr(28),
    '.': chr(55),
    '*': chr(85),
    '-': chr(86),
    '=': chr(45),
    '/': chr(84),
    '+': chr(87)
}

changingSymbols = {
    '0': chr(39),
    '1': chr(30)
}

#
# Send raw data
#

def sendData(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

#
# Writing options
#

def pressLetter(letter):
    if letter.lower() in legacySymbols:
        symbol = legacySymbols[letter.lower()]
        report = NULL_CHAR*2+symbol+NULL_CHAR*5
        if (letter.isupper()):
            report = chr(32)+NULL_CHAR+symbol+NULL_CHAR*5
        sendData(report)
        time.sleep(0.02)
        sendData(RELEASE_KEY)
        return
    if letter in changingSymbols:
        symbol = changingSymbols[letter]
        report = NULL_CHAR*2+symbol+NULL_CHAR*5
        if lang == "sk":
            report = chr(32)+NULL_CHAR+symbol+NULL_CHAR*5
        sendData(report)
        return

def writeText(text):
    for char in list(text):
        pressLetter(char)
        time.sleep(0.02)
        sendData(RELEASE_KEY)

#
# Shortcuts + letter
#

def shortcut(shortcut, letter):
    if letter.lower() in legacySymbols:
        if shortcut.lower() in shortcutsShortcut:
          shortcut = shortcutsShortcut[shortcut.lower()]
          symbol = legacySymbols[letter.lower()]
          sendData(shortcut+NULL_CHAR+symbol+NULL_CHAR*5)
          time.sleep(0.02)
          sendData(RELEASE_KEY)

# Actions

def release():
    sendData(RELEASE_KEY)

def hold(letter):
    pressLetter(letter)

def backspace():
    sendData(NULL_CHAR*2+staticKeys['backspace']+NULL_CHAR*5)
    time.sleep(0.02)
    sendData(RELEASE_KEY)
    
def enter():
    sendData(NULL_CHAR*2+staticKeys['enter']+NULL_CHAR*5)
    time.sleep(0.02)
    sendData(RELEASE_KEY)

def selectAllAndBackspace():
    shortcut("ctrl", "a")
    backspace()

def openCmd():
    shortcut("win", "r")
    time.sleep(0.2)
    selectAllAndBackspace()
    writeText("cmd")
    enter()

def shutDown():
    openCmd()
    time.sleep(2)
    writeText("shutdown /s")
    enter()

def winWithoutRelease():
    sendData(shortcutsShortcut['win']+NULL_CHAR*7)

def win():
    sendData(shortcutsShortcut['win']+NULL_CHAR*7)
    time.sleep(0.02)
    sendData(RELEASE_KEY)