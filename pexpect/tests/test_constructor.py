#!/usr/bin/env python
import pexpect
import unittest

class TestCaseConstructor(unittest.TestCase):
    #def runTest (self):
        
    def test_constructor (self):
	"""This tests that the constructor will work and give
	the same results for different styles of invoking __init__().
	This assumes that the root directory / is static during the test.
	"""
        p1 = pexpect.spawn('ls -l /bin')
        p2 = pexpect.spawn('ls' ,['-l', '/bin'])
	p1.expect (pexpect.EOF)
	p2.expect (pexpect.EOF)
	print p1.before
	print p2.before
        assert (p1.before == p2.before)

    def test_named_parameters (self):
	p = pexpect.spawn ('ls',timeout=10)
	p = pexpect.spawn (timeout=10, command='ls')
	p = pexpect.spawn (args=[], command='ls')

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(TestCaseConstructor,'test')

