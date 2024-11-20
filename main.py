

import ctypes

n=100000000


# gcc -shared -o test_c.so -fPIC app/c/test_c.c 
lib = ctypes.CDLL("app/c/test_c.so")
lib.func_1.restype = ctypes.c_longlong # ctypes 는 반환값이 기본 int 라고 생각해서 int 가 아니면 이렇게 해줘야 한다.
result_c = lib.func_1(n)
print( result_c )





def func_1(n:int):
    result = 0
    for i in range(n):
        result+=i
    return result
result_py = func_1(n)
print( result_py )
