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
     r"Well, actually you have the wrong syntax"),
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
