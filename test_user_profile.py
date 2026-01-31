"""
Tests for User Profile Settings Module
"""

import unittest
from user_profile import UserProfile


class TestUserProfile(unittest.TestCase):
    """Test cases for UserProfile class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.profile = UserProfile("testuser")
    
    def test_initialization(self):
        """Test that profile initializes with correct default settings."""
        self.assertEqual(self.profile.username, "testuser")
        self.assertEqual(self.profile.get_setting('theme'), 'light')
        self.assertEqual(self.profile.get_setting('notifications'), True)
        self.assertEqual(self.profile.get_setting('language'), 'en')
    
    def test_update_setting_success(self):
        """Test updating an existing setting."""
        result = self.profile.update_setting('theme', 'dark')
        self.assertTrue(result)
        self.assertEqual(self.profile.get_setting('theme'), 'dark')
    
    def test_update_setting_failure(self):
        """Test updating a non-existent setting."""
        result = self.profile.update_setting('invalid_key', 'value')
        self.assertFalse(result)
    
    def test_get_setting(self):
        """Test getting a setting value."""
        value = self.profile.get_setting('notifications')
        self.assertTrue(value)
    
    def test_get_setting_nonexistent(self):
        """Test getting a non-existent setting."""
        value = self.profile.get_setting('nonexistent')
        self.assertIsNone(value)
    
    def test_get_all_settings(self):
        """Test getting all settings."""
        all_settings = self.profile.get_all_settings()
        self.assertIsInstance(all_settings, dict)
        self.assertIn('theme', all_settings)
        self.assertIn('notifications', all_settings)
        self.assertIn('language', all_settings)
    
    def test_str_representation(self):
        """Test string representation of profile."""
        str_repr = str(self.profile)
        self.assertIn("testuser", str_repr)
        self.assertIn("UserProfile", str_repr)


if __name__ == '__main__':
    unittest.main()
