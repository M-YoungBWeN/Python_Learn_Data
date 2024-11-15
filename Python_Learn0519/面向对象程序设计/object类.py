"""
一切皆对象！！！！！！！！！！

"""

print(dir(object))
"""
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

"""

"""
__new__() 由系统自动调用，目的是创建一个方法 
__init__() 由程序员调用，目的是给方法初始化
__str__() 默认调用，如print(对象)会返回对象的内存地址
"""

"""
运算符也是调用的特殊方法
如加法__add__()
"""
a = 2
print(dir(a))
"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', 
'__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__',
'__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
'__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__',
'__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', 
'__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
'__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 
'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

"""
