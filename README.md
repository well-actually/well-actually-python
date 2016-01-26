# Well Actually for Python
This rando wants to lecture you on your uncaught exceptions!

In [this tweet][] I was inspired to make compile and runtime errors more annoying.
This is a wrapper around the Python interpreter that replaces exceptions in a stack
trace with more annoying messages written in a "well, actually" format. If you find
an exception that's not supported, you can [file an issue][] or [make a PR][].

[this tweet]: https://twitter.com/porglezomp/status/691748485700395009
[file an issue]: https://github.com/well-actually/well-actually-python/issues
[make a PR]: https://github.com/well-actually/well-actually-python/pulls

# Usage

To run your python scripts, do `python actually.py <script name>`.
All arguments are forwarded to Python, so you can just run `python actually.py` to get
an interactive prompt.

# Samples

```
well-actually-python $ ./actually.py test/readonly.py 
Traceback (most recent call last):
  File "test/readonly.py", line 7, in <module>
    read.foo = 1
Well actually you aren't allowed to set that attribute
```

```
well-actually-python $ ./actually.py test/attribute.py 
Traceback (most recent call last):
  File "test/attribute.py", line 2, in <module>
    a.foo
Well, int actually doesn't even have any attribute called foo
```
