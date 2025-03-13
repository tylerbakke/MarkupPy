#!/usr/bin/env python
import unittest
import sys
import os

# Add the parent directory to the path so we can import MarkupPy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import all test modules
from test_inline_features import TestInlineFeatures
from test_add_raw import TestAddRaw

if __name__ == "__main__":
    # Create a test suite with all test cases
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestInlineFeatures))
    test_suite.addTest(unittest.makeSuite(TestAddRaw))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Exit with appropriate code based on test result
    sys.exit(not result.wasSuccessful()) 