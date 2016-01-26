#!/usr/bin/env python
from subprocess import PIPE, Popen
import threading
import sys
import time
import re

replacements = [
    (re.compile(r"NameError: name '(.*)'"),
     r"Well, actually '\1' is not defined (NameError)"),
    (re.compile(r"Exception: (.*)"),
     r"Well, actually, \1 (Exception)"),
    (re.compile(r"IndexError:"),
     r"Well, actually that index is out of range (IndexError)"),
    (re.compile(r"SyntaxError:"),
     r"Well, actually you have the wrong syntax (SyntaxError)"),
    (re.compile(r"TypeError: unsupported operand type\(s\) for (.+): '(.*)' and '(.*)'"),
     r"Well actually, you can't use \1 on \2 and \3 (TypeError)"),
    (re.compile(r"TypeError: can only concatenate (.*) \(not \"(.*)\"\) to (.*)"),
     r"You're trying to concatenate \1 and \2 but you actually can't do that (TypeError)"),
    (re.compile(r"AttributeError: '(.*)' object has no attribute '(.*)'"),
     r"Well, \1 actually doesn't even have any attribute called \2"),
    (re.compile(r"AttributeError: can't set attribute"),
     r"Well actually you aren't allowed to set that attribute")
]

py = Popen(['python'] + sys.argv[1:], stdin=sys.stdin,
           stdout=sys.stdout, stderr=PIPE)


def forward_output(python_process):
    while True:
        try:
            line = python_process.stderr.readline()
            for pat, template in replacements:
                group = pat.match(line)
                if group:
                    line = group.expand(template) + '\n'
                    break
            sys.stderr.write(line)
        except Exception as e:
            raise e
            return


thread = threading.Thread(target=forward_output, name='IO Daemon',
                          args=(py,))
thread.daemon = True
thread.start()
status = py.wait()
# Wait to ensure that the error messages are all printed
# TODO: FIX THIS THIS IS HORRIBLE
time.sleep(0.01)
