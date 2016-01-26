class ReadonlyAttribute(object):
    @property
    def foo(self):
        return 0

read = ReadonlyAttribute()
read.foo = 1
