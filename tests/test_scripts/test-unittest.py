# coding=utf-8
from __future__ import absolute_import
import sys

from teamcity.unittestpy import TeamcityTestRunner
import unittest


class TestTeamcityMessages(unittest.TestCase):
    def testPass(self):
        assert 1 == 1

    def testAssertEqual(self):
        self.assertEqual("1", "2")

    def testAssertEqualMsg(self):
        self.assertEqual("1", "2", "message")

    def testAssert(self):
        self.assert_(False)

    def testFail(self):
        self.fail("failed")

    def testException(self):
        raise Exception("some exception")

    if sys.version_info >= (2, 7):
        # test skipping markup is only available since python 2.7
        # http://docs.python.org/2/library/unittest.html#skipping-tests-and-expected-failures
        @unittest.skip("Reason for skipping")
        def testSkipped(self):
            self.fail("This should not appear")


if __name__ == '__main__':
    unittest.main(testRunner=TeamcityTestRunner())
