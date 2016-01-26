# Well Actually for Python
This rando wants to lecture you on your uncaught exceptions!

In [this tweet][] I was inspired to make compile and runtime errors more annoying.
This is a wrapper around the Python interpreter that replaces exceptions in a stack
trace with more annoying messages written in a "well, actually" format.

[this tweet]: https://twitter.com/porglezomp/status/691748485700395009

To run your python scripts, do `python actually.py <script name>`.
All arguments are forwarded to Python, so you can just run `python actually.py` to get
an interactive prompt.
