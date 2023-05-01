import unittest
import numpy as np

#  from egpkg.cppfunc import timesThree

# from mypypackage import Rectangle

# from egpkg.src import func
from egpkg import timesTwo
from egpkg import timesThree

class BasicTests(unittest.TestCase):

    def test_basic1(self):
        '''Testing if two numbers are equal, just to get started
        '''
        x = 0
        y = 0
        self.assertEqual(x, y)

    def test_basic2(self):
        '''Testing if two numbers are equal, just to get started
        '''
        x = 1
        self.assertEqual(x, 1)



class TimesTwoTests(unittest.TestCase):

    def test_timesTwo1(self):
        '''Testing timesTwo
        '''
        x = 2
        soln = 4
        ans = timesTwo(x)
        self.assertEqual(ans, soln)


class TimesThreeTests(unittest.TestCase):

    def test_timesThree1(self):
        '''Testing timesThree (C++)
        '''
        x = 2
        soln = 6
        ans = timesThree(x)
        self.assertEqual(ans, soln)

