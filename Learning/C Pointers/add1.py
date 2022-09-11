import ctypes

add_lib = ctypes.CDLL('./libadd1.so')
add_one = add_lib.add
add_one.argtypes = [ctypes.POINTER(ctypes.c_int)]

x = ctypes.c_int()
add_one(ctypes.byref(x))
print(x)
