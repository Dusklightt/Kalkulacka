"""
@file mathlibtests.py
@brief Tests for TDD implementation of the math library
"""

import unittest
from mathlib import *

class Testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10, add(4,6))
        self.assertEqual(10, add(6,4))
        self.assertEqual(0, add(5,-5))
        self.assertEqual(0, add(-5,5))
        self.assertEqual(-10, add(-5,-5))
        self.assertEqual(10, add(2.2,7.8))
        self.assertEqual(10, add(7.2,2.8))
        self.assertEqual(-10, add(-2.2,-7.8))
        self.assertEqual(-10, add(-2.8,-7.2))

    def test_sub(self):
        self.assertEqual(10, sub(15,5))
        self.assertEqual(-10, sub(5,15))
        self.assertEqual(0, sub(5,5))
        self.assertEqual(0, sub(5,5))
        self.assertEqual(0, sub(-5,-5))
        self.assertEqual(-5.6, sub(2.2,7.8))
        self.assertEqual(4.4, sub(7.2,2.8))
        self.assertEqual(5.6, sub(-2.2,-7.8))
        self.assertEqual(4.4, sub(-2.8,-7.2))

    def test_mul(self):
        self.assertEqual(10, mul(2,5))
        self.assertEqual(10, mul(5,2))
        self.assertEqual(-10, mul(2,-5))
        self.assertEqual(0, mul(5,0))
        self.assertEqual(0, mul(0,5))
        self.assertEqual(25, mul(-5,-5))
        self.assertEqual(17.16, mul(2.2,7.8))
        self.assertEqual(20.16, mul(7.2,2.8))
        self.assertEqual(17.16, mul(-2.2,-7.8))
        self.assertEqual(20.16, mul(-2.8,-7.2))

    def test_div(self):
        self.assertEqual(10, div(50,5))
        self.assertEqual(1, div(5,5))
        self.assertEqual(-5, div(-10,2))
        self.assertEqual(0, div(0,5))
        self.assertEqual(1, div(-5,-5))
        self.assertEqual(0.25, div(2.2,8.8))
        self.assertEqual(4.4, div(8.8,2))
        self.assertEqual(0.25, div(-2.2,-8.8))
        self.assertEqual(4.4, div(-8.8,-2))
        self.assertRaises(ZeroDivisionError, div, 5,0)
        self.assertRaises(ZeroDivisionError, div, -5,0)
        self.assertRaises(ZeroDivisionError, div, 5.0,0)
        self.assertRaises(ZeroDivisionError, div, -5.0,0)

    def test_mod(self):
        self.assertEqual(1, mod(51,5))
        self.assertEqual(2, mod(5,3))
        self.assertEqual(1, mod(-11,2))
        self.assertEqual(0, mod(0,5))
        self.assertEqual(0, mod(-5,-5))
        self.assertEqual(2.2, mod(2.2,8.8))
        self.assertEqual(0.5, mod(8.5,2))
        self.assertEqual(-2.2, mod(-2.2,-8.8))
        self.assertRaises(ZeroDivisionError, mod, 5,0)
        self.assertRaises(ZeroDivisionError, mod, -5,0)
        self.assertRaises(ZeroDivisionError, mod, 5.0,0)
        self.assertRaises(ZeroDivisionError, mod, -5.0,0)

    def test_fact(self):
        self.assertEqual(1, fact(0))
        self.assertEqual(1, fact(1))
        self.assertEqual(2, fact(2))
        self.assertEqual(6, fact(3))
        self.assertEqual(120, fact(5))
        self.assertRaises(ValueError, fact, -1)
        self.assertRaises(ValueError, fact, 1.1)

    def test_power(self):
        self.assertEqual(1024, power(2,10))
        self.assertEqual(25, power(-5,2))
        self.assertEqual(-1000, power(-10,3))
        self.assertEqual(1, power(5,0))
        self.assertEqual(0, power(0,5))
        self.assertEqual(1, power(0,0))
        self.assertAlmostEqual(4.84, power(2.2,2))
        self.assertEqual(1024, power(16,2.5))
        self.assertAlmostEqual(4.84, power(-2.2,2))
        self.assertAlmostEqual(-10.648, power(-2.2,3))

    def test_sqrt(self):
        self.assertEqual(2, sqrt(4))
        self.assertEqual(5, sqrt(25))
        self.assertEqual(0, sqrt(0))
        self.assertEqual(1, sqrt(1))
        self.assertEqual(6, sqrt(36))
        self.assertEqual(2.5, sqrt(6.25))
        self.assertEqual(13.5, sqrt(182.25))
        self.assertRaises(ValueError, sqrt, -4)

    def test_nrt(self):
        self.assertEqual(2, nrt(4,2))
        self.assertEqual(5, nrt(25,2))
        self.assertEqual(0, nrt(0,2))
        self.assertEqual(1, nrt(1,2))
        self.assertEqual(2, nrt(8,3))
        self.assertEqual(3, nrt(27,3))
        self.assertEqual(3, nrt(81,4))
        self.assertEqual(6, nrt(36,2))
        self.assertEqual(2.5, nrt(6.25,2))
        self.assertEqual(13.5, nrt(182.25,2))
        self.assertRaises(ValueError, nrt, -4, 2)

    def test_sin(self):
        self.assertAlmostEqual(0.5, sin(30))
        self.assertEqual(1, sin(90))
        self.assertAlmostEqual(-0.5, sin(-30))
        self.assertAlmostEqual(1/(sqrt(2)), sin(45))
        self.assertEqual(0, sin(0))

if __name__ == '__main__':
    unittest.main()
