#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import readline

try:
    both_input = raw_input
except NameError:
    both_input = input

persistent_history = os.path.join(
    os.path.expanduser('~'),
    '.lemming_history'
    )

try:
    from phrases_lemming import common_phrases
except ImportError:
    common_phrases = None


def expand_phrase(message):
    prefix = message[0]
    if common_phrases and prefix in common_phrases:
        result = common_phrases[prefix] % message[1:]
    else:
        result = message
    return result


def history_start():
    readline.set_history_length(10000)
    if os.path.isfile(persistent_history):
        readline.read_history_file(persistent_history)


def history_end():
    readline.write_history_file(persistent_history)


def main():
    history_start()
    while 1:
        title = 'Commit message: '
        print(len(title) * ' ' + 50 * '-')
        message = both_input(title)
        if message:
            message = expand_phrase(message)
            command = 'git commit -m "%s"' % message
            os.system(command)
        else:
            print('Empty string - end of work.')
            break
    history_end()
