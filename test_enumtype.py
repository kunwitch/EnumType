# test_enumtype.py
"""
Tests for EnumType module.
"""

import unittest
from enumtype import EnumType

class TestEnumType(unittest.TestCase):
    """Test cases for EnumType class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EnumType()
        self.assertIsInstance(instance, EnumType)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EnumType()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
