# distutils: language = c++

cdef extern from "cppfunc.h":
    double cpp_timesThree(double x);


def timesThree(x):
    '''multiply by three
    '''
    return cpp_timesThree(x)

